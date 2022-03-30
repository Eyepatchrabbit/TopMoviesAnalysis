import os
from datetime import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

from movies.collectdata.CollectDataHelperClass import getSoupFromWebPage, getDurationInMinutes, writeOutPutFile


def getRatingsOn10Scale(scoreBoard, valueId):
    valueBasedOn100 = scoreBoard[valueId]
    return round((float(valueBasedOn100) / 10), 2)


def getDirectorsListFromMovieInfoBox(scoreBoard):
    directorsParent = scoreBoard.find("div", text="Director:").parent
    directorsFound = directorsParent.find_all("a")
    directorsList = ""
    for director in directorsFound:
        directorsList = directorsList + director.getText() + ","
    finalDirectorsList = directorsList[:-1]
    return finalDirectorsList


def getWritersListFromMovieInfoBox(scoreBoard):
    if scoreBoard.find("div", text="Writer:"):
        writersParent = scoreBoard.find("div", text="Writer:").parent
        writersFound = writersParent.find_all("a")
        writersList = ""
        for writer in writersFound:
            writersList = writersList + writer.getText() + ","
        finalWriterssList = writersList[:-1]
        return finalWriterssList
    else:
        return np.NaN


def getLanguagesFromMovieInfoBox(scoreBoard):
    languageParent = scoreBoard.find("div", text="Original Language:").parent
    originalLanguage = languageParent.find("div", {"class": "meta-value"}).getText().strip()
    return originalLanguage


def getNumberOfReviewsApproximation(soupMoviePage):
    reviewsApproximation = soupMoviePage.find("a", {'slot': "audience-count"})
    reviews = reviewsApproximation.getText().split(" ")[0].replace("+", "").replace(",", "")
    return reviews


def getBoxOfficeUsa(scoreBoard):
    if scoreBoard.find("div", text="Box Office (Gross USA):"):
        boxOfficeParent = scoreBoard.find("div", text="Box Office (Gross USA):").parent
        indicatedBoxOffice = boxOfficeParent.find("div", {'data-qa': "movie-info-item-value"}).getText() \
            .replace("$", "")
        if "K" in indicatedBoxOffice:
            numerise = float(indicatedBoxOffice.replace("K", ""))
            numerise = numerise * 1000
            return numerise
        else:
            numerise = float(indicatedBoxOffice.replace("M", ""))
            numerise = numerise * 1000000
            return numerise

        return indicatedBoxOffice

    else:
        return np.NaN


def collectDataFromMovieTable(completeUrl):
    dataFromPage = {}

    soupMoviePage = getSoupFromWebPage(completeUrl)

    # //h1[@slot="title"]
    scoreBoard = soupMoviePage.find("score-board")

    # rating Critics
    # ratingCritics = scoreBoard["tomatometerscore"]
    dataFromPage['ratingcritics'] = getRatingsOn10Scale(scoreBoard, 'tomatometerscore')
    print(f"\tRatingcritics: {dataFromPage['ratingcritics']}")

    # rating audience
    # ratingAudience = scoreBoard["audiencescore"]
    dataFromPage['ratingaudience'] = getRatingsOn10Scale(scoreBoard, 'audiencescore')
    print(f"\tRatingaudience: {dataFromPage['ratingaudience']}")

    # genres && durationminutes
    infoLine = scoreBoard.find("p", {"slot": "info"}).getText()
    splitInfoLine = infoLine.split(",")

    time = splitInfoLine[2].replace("h", ":").replace("m", "").strip().replace(' ', '')
    timeInMinutes = getDurationInMinutes(time)
    dataFromPage["durationminutes"] = timeInMinutes
    print(f"\tDurationminutes: {timeInMinutes}")

    genres = splitInfoLine[1].replace("/", ",")
    dataFromPage["genres"] = genres
    print(f"\tGenres: {genres}")

    # directors
    scoreBoard = soupMoviePage.find("ul", {"class": "content-meta info"})

    dataFromPage['directors'] = getDirectorsListFromMovieInfoBox(scoreBoard)
    print(f"\tDirectors: {dataFromPage['directors']}")

    # languages
    dataFromPage['languages'] = getLanguagesFromMovieInfoBox(scoreBoard)
    print(f"\tLanguages: {dataFromPage['languages']}")

    # countries => don't see option here

    # actor => getting just the actors here might be difficult

    # number of reviews => seems to be an "approximation"
    dataFromPage['reviews'] = getNumberOfReviewsApproximation(soupMoviePage)
    print(f"\tReviews: {dataFromPage['reviews']}")

    # boxOffice worldwide, boxOffice USA => only usa on the website and not for all movies present
    dataFromPage['boxofficeusa'] = getBoxOfficeUsa(soupMoviePage)
    print(f"\tBoxOfficeUsa: {dataFromPage['boxofficeusa']}")

    # writer/scenario
    dataFromPage['writers'] = getWritersListFromMovieInfoBox(scoreBoard)
    print(f"\tWriters: {dataFromPage['writers']}")

    return dataFromPage


def collectNeededDataFromMovie(ranking, movie):
    movieData = {}

    # collect name
    movieNameAndDate = movie.getText()
    splitting = movieNameAndDate.split("(")

    movieName = splitting[-2].replace(")", "").strip()

    movieDate = int(splitting[-1].replace(")", "").strip())

    movieData["ranking"] = ranking + 1
    movieData["name"] = movieName
    movieData["releaseYear"] = movieDate
    print(f"Movie {ranking} {movieName} ({movieDate})")

    # Find Url to moviepage
    baseUrl = "https://www.rottentomatoes.com"
    urlSuffix = movie["href"]
    completeUrl = baseUrl + urlSuffix

    print(f"\tGoing to ulr movie: {completeUrl}")

    movieData.update(collectDataFromMovieTable(completeUrl))

    return movieData


# Start of program
# -----------------------------------------------------------

# GET THE PAGE
urlTop100MoviesOffAllTime = "https://www.rottentomatoes.com/top/bestofrt/"

soup = getSoupFromWebPage(urlTop100MoviesOffAllTime)

# get list of movies to analyse
movieTable = soup.find("table", {"class": "table"})
movieList = movieTable.find_all("a", {"class": "unstyled articleLink"})

#   Gathering Data for each data in the list
movieDataGather = []

for ranking, movieLine in enumerate(movieList):
    movieDataGather.append(collectNeededDataFromMovie(ranking, movieLine))

# final list generated => create dataframe
dataFrameOfTop100Movies = pd.DataFrame(movieDataGather)

# generating output file
writeOutPutFile(dataFrameOfTop100Movies, "rottenTomatoes")
