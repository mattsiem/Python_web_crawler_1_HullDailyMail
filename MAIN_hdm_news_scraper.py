# This code has been designed by mattsiem (https://github.com/mattsiem) - Mateusz Sieminski in December 2020.
# This script is licenenced under GNU Affero General Public License v3.0.


# Imports
import requests
from bs4 import BeautifulSoup
from collections import Counter
from datetime import datetime
import pandas as pd
import time


start_time = time.time()
# Function responsible for loading predefined website and displaying page status
def loadPage():
    
    url = "https://www.hulldailymail.co.uk/news"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser' )
    targetContainer = soup.find_all("div", "teaser")
    page_status = page.status_code
    
    if page.status_code == 200:
        print("########################################")
        print("The page has been loaded successfully.", "( Page status: ", page_status ,")")
        print("########################################")
    else:
        print("########################################")
        print("An error has occured while loading the page.")
        print("########################################")
        loadPage()
        
    processData(targetContainer, soup, url)
    return 

# Function used for setting up loops for displaying blocks of scrapped data (headline titles, headline url, authors, artciles links, articles labels)
def processData(targetContainer, soup, url):

    print("--------------------------------------------------------------------------------")
    print("########################################")
    print("LIST OF ARTICLES FOUND ON THE PAGE", "(",url ,")")
    print("########################################")
    
          
    allTitles = []
    allUrl = []
    allLabel = []
    namyAll = []
    count = 0
    for a in targetContainer:
        titleX = a.find_all("a", {"class":"headline"})
        labelX = a.find_all("a", {"class":"label"})
        
        
        if not labelX:
            labelTXT = "None"
            allLabel.append(labelTXT)
        else:
            for b in labelX:
                labelTXT = b.get_text()
                allLabel.append(labelTXT)
                
        for c in titleX:
            titleTXT = c.get_text()
            urlTXT = c.get("href")
            allTitles.append(titleTXT)
            allUrl.append(urlTXT)
            
        count = count+1
            
    for linky in allUrl:
        page2 = requests.get(linky)
        soup2 = BeautifulSoup(page2.text, "html.parser")
        names = soup2.find_all("div", "author-information-container")
        if not names:
            namyTxt = "None"
            namyAll.append(namyTxt)
        else:
            for namy in names:
                namyTxt = namy.get_text()
                namyAll.append(namyTxt)
                
        print("Author: ", namyTxt)
        print("Title: ", titleTXT)
        print("Label: ", labelTXT)
        print("URL:   ", urlTXT)
        print("---------------------------------------------")

    print("--------------------------------------------------------------------------------")
    print("########################################")
    print("LIST OF LABELS USED ON THE PAGE (count in bracket)")
    print("########################################")
    
    
        
  # myList = list(dict.fromkeys(myList)) <- this is to make all list elements to be unique
  # e.g. only 1 instance of each element is in the list
  # allLabel.sort() - sorting in alphabetical order
    c = Counter(allLabel)
    c1 = Counter(allLabel).keys()
    c2 = Counter(allLabel).values()
    column1_names = (c1)
    column2_values = (c2)
    for n, v in zip(column1_names, column2_values):
        print("{} ({})".format(n, v))
        
        
    # maxLabel= max(c.items(), key=lambda k: k[1]) <- the most common key with its value (only top 1)
    # minLabel= min(c.items(), key=lambda k: k[1]) <- the least common key with its value (only top 1)
    # top3MaxLabel= sorted(c), key=c.get, reverse=True)[:3] <- top 3 keys, no values just keys printed.
    
    mc3Labels = c.most_common(3) # using counter, most common, top 3 keys with their values.
    lc3Labels = c.most_common()[:-3-1:-1] # using counter, least common top 3 keys with their values.
    print("=============================")
    print("3 most common labels: ", mc3Labels)
    print("3 least common labels: ", lc3Labels)
   
    saveData(url, allTitles, allUrl, allLabel, namyAll, start_time)
    return 
    
# Function responsible for processing the data and saving it to .xlsx file 
def saveData(url, allTitles, allUrl, allLabel, namyAll, start_time):
    
    
    #get current time
    dtNow = datetime.now()
    current_date = dtNow.strftime("%d/%m/%Y")
    current_time = dtNow.strftime("%H:%M:%S")
    
    
    #saving data to excel file
    ExcelFile = './hdmnews.xlsx'
        
    header1 = "Date"
    header2 = "Time"
    header3 = "Title"
    header4 = "Author"
    header5 = "Labels"
    header6 = "URL"
    
    df1 = pd.read_excel(ExcelFile, usecols="A:F")
    df2 = pd.DataFrame({header1:current_date, header2:current_time, header3:allTitles, header5:allLabel, header6:allUrl, header4:namyAll}) 
    updDF = df1.append(df2)
    updDF.to_excel(ExcelFile, sheet_name = "HDM_NEWS", index=False)
    
    print("########################################")
    print("The data has been successfully scraped and saved to database at",current_time , "on", current_date)
    print("########################################")
    print ("[FINISHED IN: {:.2f}s]".format(time.time() - start_time))


if __name__ == '__main__':
    loadPage()