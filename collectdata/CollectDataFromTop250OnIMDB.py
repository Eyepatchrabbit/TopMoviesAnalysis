import numpy as np
import pandas as pd

from movies.collectdata.CollectDataHelperClass import getSoupFromWebPage, getDurationInMinutes, writeOutPutFile


def extractMovieInfoFromOverviewPage(titleColumn):
    movieData = {}

    movieRank = int(titleColumn.find(text=True).strip().replace(".", ""))
    movieData["ranking"] = movieRank

    movieName = titleColumn.find("a").getText()
    movieData["name"] = movieName

    movieYear = int(titleColumn.find("span", {"class": "secondaryInfo"}).getText().replace("(", "").replace(")", ""))
    movieData["releaseYear"] = movieYear

    movieRating = float(movie.find("td", {"class": "ratingColumn imdbRating"}).getText())
    movieData["rating"] = movieRating

    print(
        f"The Movie on place {str(movieRank)} is: '{movieName}' from year {str(movieYear)} with rating {str(movieRating)}"
    )

    return movieData


def extractingGenres(soupOfPage):
    genresFoundOutput = ""
    genreSection = soupOfPage.find("li", {"data-testid": "storyline-genres"})
    genresFound = genreSection.find_all("li")
    for genre in genresFound:
        genresFoundOutput = genresFoundOutput + genre.getText() + ','

    genresFoundOutput = genresFoundOutput[:-1]
    print(f"\tFound genres: {genresFoundOutput}")
    return genresFoundOutput


def extractDurationInMinutes(soupOfPage):
    time = soupOfPage.find("li", {"data-testid": "title-techspec_runtime"})
    timeText = time.find('div').getText()
    timeDotted = timeText.replace('hours', ":").replace('hour', ":") \
        .replace('minutes', '').replace('minute', '') \
        .strip().replace(' ', '')

    print(f"\tFound Duration: {timeDotted}")
    timeInMinutes = getDurationInMinutes(timeDotted)
    return timeInMinutes


def extractDirectors(soupOfPage):
    directors = ""

    principleScreen = soupOfPage.find("div", {"data-testid": "title-pc-wide-screen"})
    if principleScreen.find(text="Director"):
        directorsBlock = principleScreen.find(text="Director").parent.parent
        directors = directorsBlock.find("a").getText()
    else:
        directorsBlock = principleScreen.find(text="Directors").parent.parent
        listDirectors = directorsBlock.find_all("a")

        for directorInList in listDirectors:
            director = directorInList.getText()
            directors = directors + f"{director},"

        directors = directors[:-1]

    print(f"\tFound following directors: {directors}")
    return directors


def extractWriters(soupOfPage):
    writers = ""

    principleScreen = soupOfPage.find("div", {"data-testid": "title-pc-wide-screen"})
    if principleScreen.find(text="Writer"):
        writerssBlock = principleScreen.find(text="Writer").parent.parent
        writers = writerssBlock.find("a").getText()
    else:
        writerssBlock = principleScreen.find(text="Writers").parent.parent
        listWriters = writerssBlock.find_all("a", {
            "class": "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"})

        for writersInList in listWriters:
            writer = writersInList.getText()
            writers = writers + f"{writer},"

        writers = writers[:-1]

    print(f"\tFound following Writers: {writers}")
    return writers


def extractOriginCountry(soupOfPage):
    countries = ""

    originCountrySection = soupOfPage.find("li", {"data-testid": "title-details-origin"})

    originCountries = originCountrySection.find_all("li")
    for countryElement in originCountries:
        country = countryElement.find("a").text
        countries = countries + f"{country},"

    countries = countries[:-1]
    print(f"\tFound following Countries of origin: {countries}")
    return countries


def extractLanguages(soupOfPage):
    languages = ""

    languagesSection = soupOfPage.find("li", {"data-testid": "title-details-languages"})

    foundlanguages = languagesSection.find_all("li")
    for languageElement in foundlanguages:
        language = languageElement.find("a").text
        languages = languages + f"{language},"

    languages = languages[:-1]
    print(f"\tFound following languages : {languages}")
    return languages


def extractActors(soupOfPage):
    actorsFound = ""

    castSection = soupOfPage.find("section", {"data-testid": "title-cast"})

    castMembers = castSection.find_all("div", {"data-testid": "title-cast-item"})
    for castMember in castMembers:
        actor = castMember.find("a", {"data-testid": "title-cast-item__actor"}).text
        actorsFound = actorsFound + f"{actor},"

    actorsFound = actorsFound[:-1]
    print(f"\tFound following actors: {actorsFound}")
    return actorsFound


def recalculateIfNeeded(budgetString, budgetNumber):
    # do approximation to Dollar so comparing apples with approximated apples
    if "$" not in budgetString:

        if "¥" in budgetString:
            budgetNumber = round(budgetNumber * 0.0082)  # based on course 26/03/2022 to get an approximation
        elif "FRF" in budgetString:
            budgetNumber = round(budgetNumber * 0.167476)  # based on course 26/03/2022 to get an approximation
        elif "€" in budgetString:
            budgetNumber = round(budgetNumber * 1.10)  # based on course 26/03/2022 to get an approximation
        elif "DEM" in budgetString:
            budgetNumber = round(budgetNumber * 0.561612)  # based on course 26/03/2022 to get an approximation
        elif "₹" in budgetString:  # indian roepies
            budgetNumber = round(budgetNumber * 0.013)  # based on course 26/03/2022 to get an approximation
        elif "£" in budgetString:
            budgetNumber = round(budgetNumber * 1.32)  # based on course 26/03/2022 to get an approximation
        elif "MVR" in budgetString:
            budgetNumber = round(budgetNumber * 0.065)  # based on course 26/03/2022 to get an approximation
        elif "₩" in budgetString: # zuid Koreaanse wong -> Ah-ga-ssi
            budgetNumber = round(budgetNumber * 0.00082)  # based on course 26/03/2022 to get an approximation
        else:
            raise Exception(f"\tThe sting doesn't contain known valuta: {budgetString}")

    return budgetNumber


def extractBoxOffice(soupOfPage, idBudgetType):
    if soupOfPage.find("li", {"data-testid": idBudgetType}):
        budgetPart = soupOfPage.find("li", {"data-testid": idBudgetType})
        budgetString = budgetPart.find("span", {"class": "ipc-metadata-list-item__list-content-item"}).getText()

        finalNumberString = ""
        for element in budgetString:
            if element.isdigit():
                finalNumberString = finalNumberString + element

        budgetNumber = recalculateIfNeeded(budgetString, int(finalNumberString))

        print(f"\tBoxOffice {idBudgetType}: {budgetNumber}")
        return budgetNumber

    print(f"\tNo Amount found for {idBudgetType}")
    return np.NaN


def extractReviews(soupOfPage):
    # find element directing to review
    ratingSection = soupOfPage.find("div", {"data-testid": "hero-rating-bar__aggregate-rating"})
    ratingSuffix = ratingSection.find("a")["href"]

    urlReviewPage = f"https://www.imdb.com{ratingSuffix}"

    print(f"\t\tGoing to the review page of movie: {urlReviewPage}")

    soupOfPageReviews = getSoupFromWebPage(urlReviewPage)

    numberOfReviews = soupOfPageReviews.find("div", {"class": "allText"}).text.split('I')[0].strip().replace(",", "")

    print(f"\t\tFound Following Number of reviews: {numberOfReviews}")

    return int(numberOfReviews)


def extractorFromMoviePage(urlMoviePage):
    print(f"\tGoing to the main page of movie: {urlMoviePage}")
    moviePageData = {}

    soupOfPage = getSoupFromWebPage(urlMoviePage)

    moviePageData["genres"] = extractingGenres(soupOfPage)
    moviePageData["durationminutes"] = extractDurationInMinutes(soupOfPage)
    moviePageData["directors"] = extractDirectors(soupOfPage)
    moviePageData["writers"] = extractWriters(soupOfPage)

    # origincountry
    moviePageData["countries"] = extractOriginCountry(soupOfPage)

    # languages
    moviePageData["languages"] = extractLanguages(soupOfPage)

    # gather data on Boxoffice worldwide gross : //li[@data-testid="title-boxoffice-cumulativeworldwidegross"] =>maybe also usa only?
    moviePageData["boxofficebudget"] = extractBoxOffice(soupOfPage, "title-boxoffice-budget")
    moviePageData["boxofficeglobal"] = extractBoxOffice(soupOfPage, "title-boxoffice-cumulativeworldwidegross")
    moviePageData["boxofficeusa"] = extractBoxOffice(soupOfPage, "title-boxoffice-grossdomestic")

    # actor
    moviePageData["actor"] = extractActors(soupOfPage)

    # gather number of reviews -> best go 1 level deeper (https://www.imdb.com/title/tt0111161/ratings/?ref_=tt_ov_rt -> )
    moviePageData["reviews"] = extractReviews(soupOfPage)

    return moviePageData


def collectNeededDataFromMovie(movie):
    movieData = {}

    titleColumn = movie.find("td", {"class": "titleColumn"})

    movieData.update(extractMovieInfoFromOverviewPage(titleColumn))

    # Go to the webPage of the movie itself now and gather additional data
    movieOverviewPage = titleColumn.find("a")["href"]
    urlToMoviePage = f"https://www.imdb.com{movieOverviewPage}"

    movieData.update(extractorFromMoviePage(urlToMoviePage))

    return movieData


# Start of program
# -----------------------------------------------------------

# GET THE STARTING PAGE
urlTop250 = "https://www.imdb.com/chart/top/"

soup = getSoupFromWebPage(urlTop250)

# GET LIST OF MOVIES ON TOP-PAGE
theListBody = soup.find("tbody")
movieList = theListBody.find_all("tr")

# Here is my advice: Accumulate data in a list, not a DataFrame.
# => Use a list to collect your data, then initialise a DataFrame when you are ready. Either a list-of-lists or list-of-dicts format will work, pd.DataFrame accepts both.
movieDataGather = []

for movie in movieList:
    movieDataGather.append(collectNeededDataFromMovie(movie))

# final list generated => create dataframe
dataFrameOfTop250Movies = pd.DataFrame(movieDataGather)

# generating output file
writeOutPutFile(dataFrameOfTop250Movies, "imdb")
