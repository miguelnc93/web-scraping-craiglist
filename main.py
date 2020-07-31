import requests, pandas
from bs4 import BeautifulSoup

request = requests.get("https://tijuana.craigslist.org/search/sss?query=rav4&sort=rel/", 
        headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
content = request.content
soup = BeautifulSoup(content,"html.parser")

""" The <li> with the clas 'result-row' is the main element 
    that contains all the information that is going to be scraped
"""
scraped_info = soup.find_all("li",{'class':'result-row'}) 

list_data=[]

for info in scraped_info:
    data = {}
    data["Fecha Publicacion"] = info.find_all("time",{'class':'result-date'})[0].text
    data["Anuncio"] = info.find_all("a",{'class':'result-title hdrlnk'})[0].text
    try:
        data["Precio"] = float(info.find_all("span",{'class':'result-price'})[0].text.replace("$","").replace(" ",""))
    except:
        data["Precio"]=None
    list_data.append(data) 
    print(data)
print("---------------------")
print(list_data)
