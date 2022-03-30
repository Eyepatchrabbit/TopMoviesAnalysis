import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

def getSoupFromWebPage(UrlToPage):
    pageData = requests.get(UrlToPage)
    # pageHtml = pageData.text.strip()
    soup = BeautifulSoup(pageData.text.strip(), 'html.parser')
    return soup

def getDurationInMinutes(timeDotted):
    timeInMinutes = 0
    if ":" in timeDotted:

        timeParts = timeDotted.split(":")
        timeInMinutes += (int(timeParts[0]) * 60)

        if timeParts[1]:
            timeInMinutes += int(timeParts[1])

    else:
        timeInMinutes = int(timeDotted)

    return timeInMinutes

def writeOutPutFile(dataFrameOfTopMovies, website):
    rootFolder = os.getcwd()
    rootFolderOutput = os.path.join(rootFolder, "outputdatagathering")
    start_time = datetime.now().strftime("%Y%m%d_%H_%M_%S")
    LocationOutputFileOfGatheredData = os.path.join(rootFolderOutput, f'dataCollected_{website}_{start_time}.csv')
    dataFrameOfTopMovies.to_csv(LocationOutputFileOfGatheredData, sep=';', index=False)