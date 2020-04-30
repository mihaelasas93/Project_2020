import pytest
from selenium import webdriver


class TestBrowser:
    # Fixture pentru Chrome browser
    @pytest.fixture(params=["chrome"], scope="class")
    def driver_init(self, request):
        if request.param == "chrome":
            #chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument("--incognito")
            #self.driver = webdriver.Chrome(chrome_options=chrome_options)
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        request.cls.driver = self.driver
        yield self.driver
        self.driver.close()
