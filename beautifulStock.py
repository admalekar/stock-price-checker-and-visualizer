from urllib.request import urlopen
from bs4 import BeautifulSoup 
import urllib.request

symbolslist = ["infy","acn"]

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
print (symbolslist)
i = 0 

for i in range(len(symbolslist)):
 url = "http://www.nasdaq.com/symbol/" + symbolslist[i]
 req = urllib.request.Request(url,headers = hdr)
 htmlfile = urlopen(req)
 htmltext = htmlfile.read().decode('utf-8')
 soup = BeautifulSoup(htmltext, "lxml")
 p = soup.find("div", attrs={"id": "qwidget_lastsale"}).text
 print (symbolslist[i] +":"+ p)
