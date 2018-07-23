import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import urllib.request
import urllib.parse

values={'q':'mahabalipuram history'}

data=urllib.parse.urlencode(values)
url='https://www.google.com/search?'+data


headers={}
headers['User-Agent']="Mozilla/5.0 (X11; Linux i686)"

req=urllib.request.Request(url,headers=headers)
resp=urllib.request.urlopen(req)
resp_data=resp.read()



soup = BeautifulSoup(resp_data, 'html.parser')
lst=soup.find_all("a")
for urlinfetchedata in lst:
    url=urlinfetchedata.get('href')
    if(url.find("http://")!=-1):
        #print(url)
        url1=str(url)
        #print("\n\n\n")
        if(url1.find("webcache")==-1):
         i=url1.find("http://")
         j=url1.find("&")
         if(j!=-1):
            print(url1[i:j])
        else:
            i = url1.find("http://",20)
            j = url1.find("&")
            print(url1[i:j])





