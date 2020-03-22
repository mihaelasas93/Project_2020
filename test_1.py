# Import the 'modules' that are required for the execution

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

#Fixture for Firefox
@pytest.fixture(params=["chrome"],scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures("driver_init")
class Test_URL():
        def test_open_url(self):
            self.driver.get("https://www.lambdatest.com/")
            #print(self.driver.title)
            page_title = self.driver.title
            assert page_title == "Cross Browser Testing Tools | Free Automated Website Testing | LambdaTest"
        def test_open_url2(self):
            self.driver.get("https://www.lambdatest.com/")
            #print(self.driver.title)
            page_title = self.driver.title
            assert page_title == "Cross Testing Tools | Free Automated Website Testing | LambdaTest"
            
        testdata=[("https://www.lambdatest.com/","M"),("https://www.lambdatest.com/","Cross Browser Testing Tools | Free Automated Website Testing | LambdaTest")]
        @pytest.mark.parametrize("a,b", testdata)
        def test_timedistance_v0(self,a, b):
            self.driver.get(a)
            #print(self.driver.title)
            page_title = self.driver.title
            assert page_title == b