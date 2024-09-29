import requests
from bs4 import BeautifulSoup #网页解析，获取数据
import re #正则表达式，进行文字匹配
import urllib.request, urllib.error #制定url，获取网页数据
import xlwt #进行excel操作
import sqlite3 #进行SQLite数据库操作
def main():
    baseurl = "https://mlh.io/seasons/2025/events"
    datalist = getData(baseurl)
    savepath = "."
    #saveData(savepath)
    askURL("https://mlh.io/seasons/2025/events")

def askURL(url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


def saveData(savepath):
    print("")#save data




def getData(baseurl):
    datalist = []
    url = baseurl
    html = askURL(url)



    return datalist

if __name__ == "__main__":
    main()



'''
def readFile(filePath):
    try:
        with open(filePath) as file:
            content = file.read()
        return content
    except Exception as result:
        pass


def writeFile(filePath,toWrite):
    try:
        with open(filePath, "w") as file:
            file.write(toWrite)
            return None
    except Exception as result:
        pass

filePath = 'write.txt'
toWrite = "abcd\ne\nf\ng\nh"
writeFile(filePath,toWrite)
fileContent = readFile(filePath)
print(fileContent)
'''
'''
f = open("write.txt", "w")
f.write("1\n2\n3")
f.close()
f = open("write.txt")
content = f.readlines()
i = 1
for temp in content:
    print("%d:%s"%(i,temp), end="")
    i += 1
f.close()
'''
