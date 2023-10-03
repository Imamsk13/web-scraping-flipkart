import requests
import pandas
from bs4 import BeautifulSoup
response = requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_2_6.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_Q1PDG4YW86MF_wp3&fm=neo%2Fmerchandising&iid=M_08ca6c58-0952-4001-b63b-bbd32a76b693_6.Q1PDG4YW86MF&ppt=hp&ppn=homepage&ssid=qx78b02a5c0000001685470809558")
# print(response)
soup=BeautifulSoup(response.content,"html.parser")
# print(soup)
names=soup.find_all('div',class_="_4rR01T")
name=[]
# print(names)
for i in names[0:10]:
    name.append(i.get_text())
print(name)

prices=soup.find_all('div',class_="_30jeq3 _1_WHN1")
price=[]
# print(names)
for i in prices[0:10]:
    price.append(i.get_text())
# print(price)

ratings=soup.find_all('div',class_="_3LWZlK")
rating=[]
# print(names)
for i in ratings[0:10]:
    rating.append(i.get_text())
# print(rating)

images=soup.find_all('img',class_="_396cs4")
image=[]
# print(names)
for i in images[0:10]:
    image.append(i['src'])
# print(image)

links=soup.find_all('a',class_="_1fQZEK")
link=[]
# print(names)
for i in links[0:10]:
    d='https://www.flipkart.com/'+ i['href']
    link.append(d)
# print(link)

df=pandas.DataFrame()
# print(df)
data={
    "names":pandas.Series(name),
    "ratings":pandas.Series(rating),
    "prices":pandas.Series(price),
    "images":pandas.Series(image),
    "links":pandas.Series(link)
}
# print(data)
df=pandas.DataFrame(data)
# print(df)
df.to_csv("mobiles.csv")