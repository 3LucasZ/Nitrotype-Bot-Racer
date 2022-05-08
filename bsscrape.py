from bs4 import BeautifulSoup

html = open("practicehtml.txt","r")
soup = BeautifulSoup(html.read(), "html.parser")

res = soup.find_all("span", class_="dash-letter")

ret=""
for letterContainer in res:
    ret+=letterContainer.text
ret = ret.replace(u'\xa0', u' ')
print(ret)
