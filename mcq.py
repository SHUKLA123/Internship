import bs4
import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import re
req = Request('https://www.learncbse.in/ncert-solutions-for-class-9-science-force-and-laws-of-motion/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soap = soup(webpage, "html.parser")
q1 = page_soap.findAll("p")
count=1
q_no = []
q = []


for i in range(0,len(q1)):
    data = q1[i].text.strip()
    datahtml = str(q1[i])
 
    q2 = q1[i].findAll("strong")

    if "option" in datahtml:
        for j in q2[0:len(q2)]:
            q.append(j.text)
            a = "\n".join(q)
            count+=1
        q_no.append(q)
    else:
            pass

df_save = pd.DataFrame({
                'questions' : q,})

with pd.ExcelWriter('question.xlsx') as writer:
    df_save.to_excel( writer, sheet_name = "all questions")
