import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DApple")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_="KzDlHZ")

name=[]
for i in names[0:20]: 
    d=i.get_text()
    name.append(d)

prices=soup.find_all('div',class_="Nx9bqj _4b5DiR")
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)

reviews=soup.find_all('div',class_="XQDdHH")
review=[]
for i in reviews[0:20]:
    d=i.get_text()
    review.append(float(d))

images=soup.find_all('img',class_="DByuf4")
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)

links=soup.find_all('a',class_="CGtC98")
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com"+i['href']
    link.append(d)

df=pd.DataFrame() # row columns
df["Names"]=name
df["Prices"]=price
df["Ratings"]=review
df["Images"]=image
df["Links"]=link

df.to_csv("Mobiles.csv")
