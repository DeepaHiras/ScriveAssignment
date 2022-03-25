import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


def getdriverfirefox():
    s = Service(executable_path='./geckodriver')
    driver = webdriver.Firefox(service=s)
    return driver


def getdriverchrome():
    s = Service(executable_path='./chromedriver')
    driver = webdriver.Chrome(service=s)
    return driver


def getdriverbrowserstack():
    options = webdriver.IeOptions()
    options.set_capability('browser_version', '11.0')
    options.set_capability('name', 'Scrive')
    options.set_capability('build', 'Scrive')
    driver = webdriver.Remote(
        command_executor='https://deepahiras_vdzJ23:sQGpGhs3rAKUcPxeUs4k@hub-cloud.browserstack.com/wd/hub',
        options=options)
    return driver


def tests(driver, browser):
    driver.get('https://staging.scrive.com/t/9221714692410699950/7348c782641060a9')
    driver.find_element(By.ID, 'name').send_keys('Test Assignment')
    driver.find_element(By.LINK_TEXT, 'Next').click()
    time.sleep(3)
    if browser == 'chrome':
        driver.save_screenshot('Screenshots/Chrome-ConfirmationModel.png')
    if browser == 'firefox':
        driver.save_screenshot('Screenshots/Firefox-ConfirmationModel.png')
    if browser == 'browserstack':
        driver.save_screenshot('Screenshots/BrowserStack-ConfirmationModel.png')
    WebDriverWait(driver, 10).until(
        presence_of_element_located((By.LINK_TEXT, 'Sign'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        presence_of_element_located((By.XPATH, "//*[contains(text(), 'Document signed!')]")))
    if browser == 'chrome':
        driver.save_screenshot('Screenshots/Chrome-DocumentSigned.png')
    if browser == 'firefox':
        driver.save_screenshot('Screenshots/Firefox-DocumentSigned.png')
    if browser == 'browserstack':
        driver.save_screenshot('Screenshots/BrowserStack-DocumentSigned.png')
    driver.close()
    driver.quit()
