	
# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    source = requests.get("https://coinmarketcap.com").text
    soup = BeautifulSoup(source, "html.parser")
    hotKeys = soup.select_one("#__next > div > div.main-content > div.sc-1ojz83d-0.fLfsZi > div:nth-child(2) > div > div.sc-18ghxad-0.ifvooB > div > div.cmc-global-stats__content > div > span:nth-child(3) > a")
    name = hotKeys.text
    hotKeys2 = soup.select_one("#__next > div > div.main-content > div.sc-1ojz83d-0.fLfsZi > div:nth-child(2) > div > div.sc-18ghxad-0.ifvooB > div > div.cmc-global-stats__content > div > span:nth-child(5) > a")
    name2 = hotKeys2.text


    source2 = requests.get("https://coinmarketcap.com/currencies/bitcoin/").text
    soup2 = BeautifulSoup(source2, "html.parser")
    hotKeys3 = soup2.select_one("#__next > div > div.main-content > div.sc-57oli2-0.dEqHl.cmc-body-wrapper > div > div.sc-16r8icm-0.hNsOU.container > div.sc-16r8icm-0.kXPxnI.container___lbFzk > div.sc-16r8icm-0.kXPxnI.priceSection___3kA4m > div.sc-16r8icm-0.kXPxnI.priceTitle___1cXUG > div")
    name3 = hotKeys3.text

    source3 = requests.get("https://coinmarketcap.com/currencies/bitcoin/").text
    soup3 = BeautifulSoup(source3, "html.parser")
    hotKeys4 = soup3.select_one("#__next > div > div.main-content > div.sc-57oli2-0.dEqHl.cmc-body-wrapper > div > div.sc-16r8icm-0.hNsOU.container > div.sc-16r8icm-0.kXPxnI.container___lbFzk > div.sc-16r8icm-0.iTsqJR.statsSection___2aZ29 > div.hide___2JmAL.statsContainer___2uXZW > div:nth-child(1) > div > div.statsItemRight___yJ5i- > span")
    if "--down-color" in str(hotKeys4):
        name4 = "-" + hotKeys4.text
    else:
        name4 = "+" + hotKeys4.text

    return render_template('index.html',data=name,data2=name2,data3=name3,data4=name4)

@app.route('/about')
def about():
    return 'About 페이지'