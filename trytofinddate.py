import requests
from bs4 import BeautifulSoup #网页解析，获取数据
import re #正则表达式，进行文字匹配
import urllib.request, urllib.error #制定url，获取网页数据
import xlwt #进行excel操作
import sqlite3 #进行SQLite数据库操作
def main():
    baseurl = "https://hack.gt/"
    # datalist = getData(baseurl)
    # savepath = "."
    # #saveData(savepath)
    apply = ["apply","application"]
    printHTML(baseurl,apply)

def printHTML(url, apply):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        bs = BeautifulSoup(html, "html.parser")
        href = ""
        for word in apply:
            elements = bs.find_all()
            matching_elements = []
            for element in elements:
                if element.string and word.lower() in element.string.lower():
                    matching_elements.append(element)
                if matching_elements:
                    #print(f"Elements containing '{word}':")
                    for match in matching_elements:
                        if 'href' in match.attrs:
                            href =match['href']
                            #print(match.prettify())  # Print nicely formatted HTML
        print(href)
    except Exception as e:
        return html


# def saveData(savepath):
#     print("")#save data




def getData(baseurl):
    datalist = []
    url = baseurl
    html = printHTML(url)



    return datalist

if __name__ == "__main__":
    main()
