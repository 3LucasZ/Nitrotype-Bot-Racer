from bs4 import BeautifulSoup

html = open("practicehtml.txt","r")
soup = BeautifulSoup(html.read(), "html.parser")

res = soup.find(class_="racev3-chat")
if res == None:
    print("Begin!")
else:
    print("Waiting...",res.text)