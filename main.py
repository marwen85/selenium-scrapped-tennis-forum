import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime as dt
import os
import sys

application_path= os.path.dirname(sys.executable)

now = dt.now()
date = now.strftime('%d%m%Y')


path = 'C:/Users/marwen/Desktop/MongoDB/chromedriver/chromedriver.exe'
website = 'https://www.tennisforum.com/search/608719/?q=ons+jabeur&o=date'
option= Options()
option.headless= True
driver = webdriver.Chrome(executable_path=path, options= option)
driver.get(website)

#//div[@class="contentRow-main"]

containers = driver.find_elements(by='xpath', value='//div[@class="contentRow-main"]')
titles =[]
subtitles = []
links = []

for container in containers:
    Title = container.find_element(by='xpath', value='//div[@class="contentRow-main"]/div/h3').text
    subtitle = container.find_element(by='xpath', value='//div[@class="contentRow-snippet no-italic mb-10"]').text
    link = container.find_element(by='xpath', value='//div[@class="contentRow-main"]/div/h3/a').get_attribute('href')
    titles.append(Title)
    subtitles.append(subtitle)
    links.append(link)

print(subtitles)

mydict = {'titles': titles, 'subtitle': subtitles, 'links': links}

tf_ons = pd.DataFrame(mydict)
file_name = f'tf_onsjabeur {date}'
final_name = os.path.join(application_path, file_name)
tf_ons.to_csv(final_name)