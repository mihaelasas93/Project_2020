import pytest
import selenium
import time
from common_files.test_web_driver import TestBrowser


@pytest.mark.usefixtures("driver_init")
class TestSuiteSecurity(TestBrowser):
    html_address_main_page = "http://automationpractice.com/"

    @pytest.mark.login_page
    @pytest.mark.security_suite
    def test_password_limitations(self):
        self.driver.get(self.html_address_main_page)
        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
        time.sleep(2)  # page transition
        email_area = self.driver.find_element_by_id('email')
        email_area.send_keys("sarah_jon@yahoo.com")
        i = 10
        while i > 0:
            password_area = self.driver.find_element_by_id('passwd')
            parola = "parolaacunsa"+str(i)
            password_area.clear()
            password_area.send_keys(parola)
            self.driver.find_element_by_xpath(
                '//*[@id="SubmitLogin"]/span').click()
            time.sleep(3)  # wait
            i -= 1
        time.sleep(10)  # wait
        text = self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/div[1]/ol/li').text
        assert text == "The acount was locked."

    @pytest.mark.login_page
    @pytest.mark.security_suite
    def test_invalid_address_text(self):
        self.driver.get(self.html_address_main_page)
        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
        time.sleep(2)  # page transition
        email_area = self.driver.find_element_by_id('email')
        email_area.send_keys("sarah_jon@yahoo.com")
        i = 10
        while i > 0:
            password_area = self.driver.find_element_by_id('passwd')
            parola = "e"+str(i)
            password_area.clear()
            password_area.send_keys(parola)
            self.driver.find_element_by_xpath(
                '//*[@id="SubmitLogin"]/span').click()
            time.sleep(3)  # wait
            i -= 1
        time.sleep(10)  # wait
        text = self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/div[1]/ol/li').text
        counter = 0
        if "Invalid password" in text:
            counter += 1
        assert counter == 0, "Invalid passworld text appeared more than one time"

    @pytest.mark.login_page
    @pytest.mark.security_suite
    def test_user_not_logout_after_back_action(self):
        self.driver.get(self.html_address_main_page)
        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
        time.sleep(2)  # page transition
        email_area = self.driver.find_element_by_id('email')
        email_area.send_keys("sarah_jon@yahoo.com")
        password_area = self.driver.find_element_by_id('passwd')
        password_area.send_keys("sarahjon")
        self.driver.find_element_by_xpath(
            '//*[@id="SubmitLogin"]/span').click()
        time.sleep(2)  # page transition
        self.driver.back()
        self.driver.back()
        time.sleep(10)  # page transition
        try:
            user_name = self.driver.find_element_by_xpath(
                '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span').text
            assert user_name == "Sarah Jon"
        except:
            assert False, "User was logouted after back actions"

    @pytest.mark.main_page
    @pytest.mark.security_suite
    def test_user_session_timeout(self):
        self.driver.get(self.html_address_main_page)
        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
        time.sleep(2)  # page transition
        email_area = self.driver.find_element_by_id('email')
        email_area.send_keys("sarah_jon@yahoo.com")
        password_area = self.driver.find_element_by_id('passwd')
        password_area.send_keys("sarahjon")
        self.driver.find_element_by_xpath(
            '//*[@id="SubmitLogin"]/span').click()
        time.sleep(1000)  # timeout
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=my-account"
