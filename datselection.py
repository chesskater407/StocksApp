
pip install selenium

import chromedriver_install as cdi
path = cdi.install(file directory='c:\\Program Files\\Google\\Chrome\\Application', verbose=True, chmod=True, overwrite=False, version=None)
print('Installed chromedriver to path: %s' % path)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome

driver.get("https://finance.yahoo.com")

        
        
text_area = driver.find_element_by_xpath('//header[not(contains(@class, "clone"))]//div[@id="search"]//input')


