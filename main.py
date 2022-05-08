from selenium import webdriver
from selenium.webdriver.common.by import By
import cred
import pyautogui
from bs4 import BeautifulSoup
import time

driver = webdriver.Remote(command_executor=cred.URL, desired_capabilities={})
driver.close()
driver.session_id=cred.SESSION_ID

driver.get("https://www.nitrotype.com/race")

print("Press enter when ready")
x = input()
pyautogui.click(200,200)

# for i in range(4):
#     paragraph = ""
#     letters = driver.find_elements(by=By.CLASS_NAME, value="dash-letter")
#     for letter in letters:
#         paragraph+=letter.text
#     paragraph = paragraph.replace(u'\xa0', u' ')
#     print(paragraph)
#     pyautogui.write(paragraph, interval=0.001)
html = driver.page_source
time.sleep(2)
soup = BeautifulSoup(html, "html.parser")
res = soup.find_all("span", class_="dash-letter")
ret=""
for letterContainer in res:
    ret+=letterContainer.text
ret = ret.replace(u'\xa0', u' ')
print(ret)
time.sleep(1)
pyautogui.write(ret, interval=0.04)
"racev3-chat"