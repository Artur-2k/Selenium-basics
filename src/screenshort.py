# from library selenium, import  class webdriver
# Webdriver is the main component of selenium that allows to control a browser
from selenium import webdriver
# Service is a way of managing the driver process.
from selenium.webdriver.firefox.service import Service 
# By is used to specify how to locate elements on a webpage. It is a common utility in Selenium
from selenium.webdriver.common.by import By
# Options is a class used to customize the Firefox browser's behavior when starting a WebDriver session.
from selenium.webdriver.firefox.options import Options


# create a service object to manage the geckodriver executable
service = Service(executable_path='/snap/bin/geckodriver')

# create an options object to customize firefox's behaviour
options = Options()
options.add_argument('--headless') # no UI

# initialize the webdriver with the service and options
driver = webdriver.Firefox(service=service, options=options)

# enters the site with URL
driver.get('https://www.tribalwars.com.pt/')

# performs a screenshot and saves it on this path
driver.save_screenshot('tribos.png')

# clears everything about the driver cleanly
driver.quit()