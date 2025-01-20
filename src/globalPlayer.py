from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# configuração para usar o firefox
options = Options()
options.set_preference("dom.webdriver.enabled", False)  # Desativa o modo de detecção de automação
options.set_preference("useAutomationExtension", False)  # Desativa a extensão de automação

service = Service(executable_path='/snap/bin/geckodriver')

driver = webdriver.Firefox(options=options, service=service)

driver.get('https://www.tribalwars.com.pt/')

# waits for max 10 seconds beore an action
wait = WebDriverWait(driver, 10)

# show 
langSelector = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'pb-lang-select')))
langSelector.click()

dropdown = driver.find_element(By.CLASS_NAME, 'pb-lang-sec-options')
langs = dropdown.find_elements(By.TAG_NAME, 'li')

hrefs = []

for lang in langs:
    anchor = lang.find_element(By.TAG_NAME, 'a')
    href = anchor.get_attribute('href')
    hrefs.append(href)

with open('global.txt', 'w', encoding='utf-8') as file:
    for ref in hrefs:
        try:
            driver.get(ref)

            worldInfo = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headerlink-stats"]')))
            worldInfo.click()

            noPlayers = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.data-table > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)'))).text
            file.write(f"{ref} : {noPlayers}\n")
        except TimeoutException:
                print('wtf is going on xDDD')

# clean the webdriver
driver.quit()