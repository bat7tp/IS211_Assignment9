import requests
from bs4 import BeautifulSoup

url = "http://www.footballlocks.com/nfl_point_spreads.shtml"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

table = soup.find_all('table', cols='4')
# print(table)

# text = tr.text
# print(text)

info = table[0].text
# print(one.text)



# for trs in table:

tr = table[0].find_all('tr')
# print(tr)

# td = tr[1].find_all('td')
# print(td[2])


for i in range(len(tr)):
    td = tr[i].find_all('td')
    number = str(i)

    spread = td[2].text
    underdog = td[3].text
    favorite = td[1].text

    print("Week " + number + ":")
    print("The favorite was: " + favorite)
    print("The spread was: " + spread)
    print("The underdog was: " + underdog)

