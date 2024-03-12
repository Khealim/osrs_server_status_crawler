import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def table_printer(data_dict):
    data_string = 'Fellow osrs enjoyer!!\nPlease be aware that the following server maintenances will happen in the future that we are aware of:\n'
    header = []
    for key,values in iter(data_dict.items()):
        if key == 'header':
            for value in values:
                header.append(value)
    for key,values in iter(data_dict.items()):
        if key != 'header':
            i = 0
            data_string += str(key) +'.\n'
            for value in values:
                data_string += header[i] + ' | ' + value + '\n'
                i+=1
    
    return data_string

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

driver.get("https://secure.runescape.com/m=news/game-status-information-centre?oldschool=1")

table_element = driver.find_element(By.XPATH, "//table")

# Find the tbody element inside the table
tbody_element = table_element.find_element(By.XPATH, "./tbody")

# Find all tr elements inside the tbody
tr_elements = tbody_element.find_elements(By.XPATH, "./tr")

i = 0
data = {}
for elem in tr_elements:
    td_elements = elem.find_elements(By.XPATH, "./td")
    for td in td_elements:
        if i == 0:
            if 'header' in data:
                data['header'].append(td.get_attribute("textContent"))
            else:
                data['header'] = [td.get_attribute("textContent")]
        else:
            if i in data:
                data[i].append(td.get_attribute("textContent"))
            else:
                data[i] = [td.get_attribute("textContent")]
    i += 1
        

print(table_printer(data))

url = "https://discord.com/api/v9/channels/1053737293011234888/messages"

payload = {
    "content" : table_printer(data)
}

headers = {
    "Authorization": ""
}

res = requests.post(url,payload,headers=headers)

