import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import re
req = Request('https://www.learncbse.in/ncert-solutions-for-class-9-science-force-and-laws-of-motion/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soap = soup(webpage, "html.parser")
q1 = page_soap.findAll("p")

for i in range(0,len(q1)):
  if "option" in q1[i].text:
    q2 = q1[i].findAll("strong")
    for j in q2[0:len(q2)]:
      print(j.text)
      print("\n")
      
    print("\n")
    print("********************************************")
    print("\n")  

  else:
    pass
