from selenium.common.exceptions import NoSuchElementException

import TestFlow

try:

    # Testing in Chrome
    driver = TestFlow.getdriverchrome()
    TestFlow.tests(driver, 'chrome')

    # Testing in Firefox
    driver = TestFlow.getdriverfirefox()
    TestFlow.tests(driver, 'firefox')

    # Testing in BrowserStack
    driver = TestFlow.getdriverbrowserstack()
    TestFlow.tests(driver, 'browserstack')

except NoSuchElementException:
    print('Element was not loaded')
