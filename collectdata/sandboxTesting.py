from movies.collectdata.CollectDataHelperClass import getSoupFromWebPage

import re

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

soupOfPage = getSoupFromWebPage("https://www.imdb.com/title/tt7131622/")
# soupOfPage = getSoupFromWebPage("https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=YKBRPKP2EB3WY7KP64RJ&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1")
# soupOfPage = getSoupFromWebPage("https://www.imdb.com/title/tt0468569/")

idBudgetType = "title-boxoffice-budget"

if soupOfPage.find("li", {"data-testid": idBudgetType}):
    budgetPart = soupOfPage.find("li", {"data-testid": idBudgetType})
    budgetString = budgetPart.find("span", {"class": "ipc-metadata-list-item__list-content-item"}).getText()

    finalNumberString = ""
    for element in budgetString:
        if element.isdigit():
            finalNumberString = finalNumberString + element

    budgetNumber = recalculateIfNeeded(budgetString, int(finalNumberString))

    print(f"\tBoxOffice {idBudgetType}: {budgetNumber}")
#     return budgetNumber
#
# print(f"\tNo Amount found for {idBudgetType}")
# return np.NaN
