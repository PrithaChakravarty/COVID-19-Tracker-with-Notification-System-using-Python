from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\cprit\\Desktop\\COVIDNOTIFY\\icon.ico",
        timeout = 4

    )

def getData(url):
    r = requests.get(url)
    return r.text



if __name__ == '__main__':
    # notifyMe("Pritha", "Let's stop this corona virus pandemic together")
    while True:
        myHtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")
        # print(itemList)
        states = ['West Bengal', 'Karnataka']
        for item in itemList[0:36]:
            dataList = (item.split('\n'))
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of Covid-19'
                nText = f"State : {dataList[1]}\nActive Cases : {dataList[2]} & Cured : {dataList[3]}\nDeaths: {dataList[4]}\nTotal Cases : {dataList[5]}"
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(10)
        


    