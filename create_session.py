from selenium import webdriver

chrome_driver_path = "/Users/lucaszheng/Projects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url=driver.command_executor._url
session_id = driver.session_id

print(url)
print(session_id)

f = open("cred.py", "w")
f.write('DRIVER_PATH="/Users/lucaszheng/Projects/chromedriver"\n')
f.write('URL="'+url+'"\n')
f.write('SESSION_ID="'+session_id+'"\n')