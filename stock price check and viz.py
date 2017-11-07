import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import urllib.request


#TODO ask the user the enter the list. Use this list for now.
symbolslist = ["infy","aapl"]

#creating a header incase script is not allowed to scrap
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
print (symbolslist)


style.use('classic')

#Arbitrary start and end dates to be used for data visualization
start = dt.datetime(2010,1,1)
end = dt.datetime(2016,1,1)

i = 0 
#loop for the number of symbols in the list
for i in range(len(symbolslist)):

 #getting stock price data from nasdaq 
 url = "http://www.nasdaq.com/symbol/" + symbolslist[i]
 req = urllib.request.Request(url,headers = hdr)
 htmlfile = urlopen(req)
 htmltext = htmlfile.read().decode('utf-8')
 soup = BeautifulSoup(htmltext, "lxml")
 p = soup.find("div", attrs={"id": "qwidget_lastsale"}).text
 print (symbolslist[i] +":"+ p)
 
 # getting historic data from yahoo
 df = web.get_data_yahoo(symbolslist[i],start,end)
 
 #creating csv
 df.to_csv(symbolslist[i] + '.csv')
 
 #reading the csv
 df = pd.read_csv(symbolslist[i]+'.csv',parse_dates = True, index_col=0)

 df.plot()
 plt.show()
 



