from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# configuração para usar o firefox
options = Options()
options.set_preference("dom.webdriver.enabled", False)  # Desativa o modo de detecção de automação
options.set_preference("useAutomationExtension", False)  # Desativa a extensão de automação

service = Service(executable_path='/snap/bin/geckodriver')

driver = webdriver.Firefox(options=options, service=service)

driver.get('https://www.tribalwars.com.pt/')

# waits for max 10 seconds beore an action
wait = WebDriverWait(driver, 10)

# will wait until the element given with XPath is ready to be clicked
worldInfo = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headerlink-stats"]')))
worldInfo.click()  # Clica no link "Informação do Mundo"

noPlayers = driver.find_element(By.CSS_SELECTOR, '.data-table > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)').text

# opens with the with keyword so we dont need to file.close and its safer
#           name            write mode   utf-8 encoding
with open("playerBase.txt", 'w', encoding='utf-8') as file:
    file.write(noPlayers + '\n') # write method


# clean the webdriver
driver.quit()


