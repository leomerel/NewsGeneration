from bs4 import BeautifulSoup as soup
import requests
import json

def getContent(url):
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    pageSoup = soup(page.content, 'html.parser')
    # print(pageSoup)

    containers = pageSoup.find_all("div", {"class" : "content-list-component yr-content-list-text text"})

    if len(containers) == 0 :
        containers = pageSoup.find_all("div", {"class" : "primary-cli cli cli-text"})    

    textList = []

    for container in containers :
        for div in container :
            if div.name == 'p':
                if div.text != "" :
                    textList.append(div.text)

    text = ""
    for t in textList:
        text += str(t)

    # print(text)
    print()

    wordCount = len(text.split())
    print("Total words : " + str(wordCount))
    
    return text,wordCount
