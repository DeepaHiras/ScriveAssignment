from selenium.common.exceptions import NoSuchElementException

import TestFlow

try:

    # Testing in Chrome
    driver = TestFlow.getdriverchrome()
    TestFlow.tests(driver, 'chrome')
    print('Tested successfully in Chrome')

    # Testing in Firefox
    driver = TestFlow.getdriverfirefox()
    TestFlow.tests(driver, 'firefox')
    print('Tested successfully in Firefox')

    try:
        # Testing in BrowserStack
        driver = TestFlow.getdriverbrowserstack()
        TestFlow.tests(driver, 'browserstack')
        print('Tested successfully in BrowserStack')
    except:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Failed"}}')
    else:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Passed"}}')

    driver.quit()

except NoSuchElementException:
    print('Exception: Some element was not loaded. Tests incomplete')
except:
    print('Something went wrong. Tests Incomplete')
