#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

url = 'https://www.worldometers.info/coronavirus/country/india/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

news = soup.find("li",{"class":"news_li"})
cases = news.find_all("strong")[0].text.split()[0]
death = news.find_all("strong")[1].text.split()[0]

notifier = ToastNotifier()
message = "New Cases -----> " + cases + "\nDeath -----> " + death

notifier.show_toast(title="COVID-19 STATUS", msg=message, duration=10, icon_path="coronavirus.ico")
