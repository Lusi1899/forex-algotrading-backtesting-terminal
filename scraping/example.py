from bs4 import BeautifulSoup

with open('index.html',"r") as f:
    data=f.read()

# print(data)
soup= BeautifulSoup(data, 'html.parser')

# print(soup)

divs=soup.select("div")

print("Content:",divs[0].get_text())
divs2=divs[1]
pps=divs2.select("p")

for p in pps:
    print(p.get_text())