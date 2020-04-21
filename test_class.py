import pytest
from selenium import webdriver

# Fixture pentru Chrome browser
@pytest.fixture(params=["chrome"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()


@pytest.mark.usefixtures("driver_init")
class TestClass:
    def test_open_url(self):
        self.driver.get("http://automationpractice.com/")
        assert self.driver.title == "My Store"

    def test_open_url2(self):
        self.driver.get(
            "http://automationpractice.com/index.php?controller=order")
        assert self.driver.title == "Order - My Store"
