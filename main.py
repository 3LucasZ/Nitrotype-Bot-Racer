from selenium import webdriver
from selenium.webdriver.common.by import By
import cred
import pyautogui

driver = webdriver.Remote(command_executor=cred.URL, desired_capabilities={})
driver.close()
driver.session_id=cred.SESSION_ID

driver.get("https://www.nitrotype.com/race")

print("Press enter when ready")
x = input()
pyautogui.click(200,200)

for i in range(4):
    paragraph = ""
    letters = driver.find_elements(by=By.CLASS_NAME, value="dash-letter")
    for letter in letters:
        paragraph+=letter.text
    paragraph = paragraph.replace(u'\xa0', u' ')
    print(paragraph)
    pyautogui.write(paragraph, interval=0.001)