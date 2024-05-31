from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get('https://www.youtube.com/')
driver.maximize_window()
sleep(5)

search = driver.find_element(By.NAME, "search_query")
search.clear()
search.send_keys("Launch of LVM3-M4/CHANDRAYAAN-3 Mission from Satish Dhawan Space Centre (SDSC) SHAR, Sriharikota")
search.send_keys(Keys.ENTER)
sleep(5)

link = driver.find_element(By.XPATH, '//*[@id="video-title"]')
link.click()
sleep(20)

for i in range(2):
    driver.execute_script("window.scrollBy(0,700)","")
    sleep(2)

sleep(20)

comment_list = []

comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
for comment in comments:
    comment_list.append(comment.text)

print(comment_list)
print(len(comment_list))

df = pd.DataFrame({"comment": comment_list})
df.to_csv("youtube_comments.csv", index=False)

assert "No results found." not in driver.page_source
driver.close()
