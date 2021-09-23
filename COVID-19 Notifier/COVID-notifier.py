"""
    COVID-19 Status
    - Get notification of new cases and deaths

    Author : Sudhanshu Motewar
    Date   : 21/03/21
"""

import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

# get your country url here https://www.worldometers.info/coronavirus/
url = 'https://www.worldometers.info/coronavirus/country/india/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# get the tag where death and cases is located
news = soup.find("li",{"class":"news_li"})
cases = news.find_all("strong")[0].text.split()[0]
death = news.find_all("strong")[1].text.split()[0]

# created object of ToastNotifier()
notifier = ToastNotifier()
message = "New Cases -----> " + cases + "\nDeath -----> " + death

# it gives notification
notifier.show_toast(title="COVID-19 STATUS", msg=message, duration=10, icon_path="coronavirus.ico")
