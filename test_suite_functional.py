import pytest
import selenium
import time
from common_files.test_web_driver import TestBrowser
from flaky import flaky


@pytest.mark.usefixtures("driver_init")
class TestSuiteFunctional(TestBrowser):
    html_address_main_page = "http://automationpractice.com/"
    @flaky
    @pytest.mark.login_page
    @pytest.mark.functional_suite
    def test_create_new_user(self):
        self.driver.get(self.html_address_main_page)
        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()

        time.sleep(2)  # page transition
        email_area = self.driver.find_element_by_id('email_create')
        email_area.send_keys("qwerty123@yahoo.com")
        self.driver.find_element_by_xpath(
            '// *[@id="SubmitCreate"]/span').click()
        time.sleep(2)  # page transition
        assert self.driver.title == "Login - My Store"

    @flaky
    @pytest.mark.login_page
    @pytest.mark.functional_suite
    def test_create_new_user_which_exists(self):
        self.driver.get(self.html_address_main_page)
        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()

        time.sleep(2)  # page transition
        email_area = self.driver.find_element_by_id('email_create')
        email_area.send_keys("sarah_jon@yahoo.com")
        self.driver.find_element_by_xpath(
            '// *[@id="SubmitCreate"]/span').click()
        time.sleep(3)  # wait
        element = self.driver.find_element_by_xpath(
            '//*[@id="create_account_error"]/ol/li')
        assert not element.is_displayed()

    @flaky
    @pytest.mark.login_page
    @pytest.mark.functional_suite
    def test_password_masked(self):
        self.driver.get(self.html_address_main_page)
        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
        time.sleep(2)  # page transition
        email_area = self.driver.find_element_by_id('email')
        email_area.send_keys("a@yahoo.com")
        password_area = self.driver.find_element_by_id('passwd')
        password_area.send_keys("parolaacunsa")
        pw_type = password_area.get_attribute("type")
        assert pw_type == "password", "Your password is masked!"

    @flaky
    @pytest.mark.login_page
    @pytest.mark.functional_suite
    def test_wrong_password(self):
        self.driver.get(self.html_address_main_page)
        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
        time.sleep(2)  # page transition
        email_area = self.driver.find_element_by_id('email')
        email_area.send_keys("a@yahoo.com")
        password_area = self.driver.find_element_by_id('passwd')
        password_area.send_keys("parolaacunsa")
        self.driver.find_element_by_xpath(
            '//*[@id="SubmitLogin"]/span').click()

        text = self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/div[1]/ol/li').text
        assert text == "Authentication failed."

    @flaky
    @pytest.mark.login_page
    @pytest.mark.functional_suite
    def test_invalid_address(self):
        self.driver.get(self.html_address_main_page)
        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
        time.sleep(2)  # page transition
        email_area = self.driver.find_element_by_id('email')
        email_area.send_keys("aaaaaaaaaaa@yahoo.com")
        self.driver.find_element_by_xpath(
            '//*[@id="SubmitLogin"]/span').click()

        text = self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/div[1]/ol/li').text
        assert text == "Invalid e-mail address."

    @flaky
    @pytest.mark.login_page
    @pytest.mark.functional_suite
    def test_no_password(self):
        self.driver.get(self.html_address_main_page)
        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
        time.sleep(2)  # page transition
        email_area = self.driver.find_element_by_id('email')
        email_area.send_keys("qwerty123@yahoo.com")
        password_area = self.driver.find_element_by_id('passwd')
        password_area.send_keys("parolaacunsa")
        self.driver.find_element_by_xpath(
            '//*[@id="SubmitLogin"]/span').click()

        text = self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/div[1]/ol/li').text
        assert text == "Password is required."

    @flaky
    @pytest.mark.login_page
    @pytest.mark.functional_suite
    def test_forgot_password(self):
        self.driver.get(self.html_address_main_page)
        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
        time.sleep(2)  # page transition
        email_area = self.driver.find_element_by_id('email')
        email_area.send_keys("qwerty123@yahoo.com")
        self.driver.find_element_by_xpath(
            '//*[@id="login_form"]/div/p[1]/a').click()
        assert self.driver.title == " Forgot your password - My Store"

    @flaky
    @pytest.mark.my_account
    @pytest.mark.functional_suite
    def test_login_with_valid_adrress(self):
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
        assert self.driver.title == " My account - My Store"

    @flaky
    @pytest.mark.my_account
    @pytest.mark.functional_suite
    def test_account_wishlist(self):
        self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/div/div[2]/ul/li/a/span').click()
        time.sleep(2)  # page transition
        assert self.driver.title == "Wishlist - My Store"
        self.driver.back()

    @flaky
    @pytest.mark.my_account
    @pytest.mark.functional_suite
    def test_account_order_history(self):
        self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/div/div[1]/ul/li[1]/a/span').click()
        time.sleep(2)  # page transition

        text = self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/h1').text
        assert text == "ORDER HISTORY"
        self.driver.back()

    @flaky
    @pytest.mark.my_account
    @pytest.mark.functional_suite
    def test_account_personal_info(self):
        self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/div/div[1]/ul/li[4]/a/span').click()
        time.sleep(2)  # page transition

        text = self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/div/h1').text
        assert text == "YOUR PERSONAL INFORMATION"
        self.driver.back()

    @flaky
    @pytest.mark.my_account
    @pytest.mark.functional_suite
    def test_account_address_details(self):
        self.driver.find_element_by_xpath(
            '//*[@id= "center_column"]/div/div[1]/ul/li[3]/a/span').click()
        time.sleep(2)  # page transition
        assert self.driver.title == "My address - My Store"
        self.driver.back()

    @flaky
    @pytest.mark.my_account
    @pytest.mark.functional_suite
    def test_add_an_item_to_cart(self):
        search_area = self.driver.find_element_by_id('search_query_top')
        search_area.send_keys("printed")
        self.driver.find_element_by_xpath(
            '//*[@id="searchbox"]/button').submit()
        time.sleep(2)  # page transition
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(10)  # page transition
        self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img').click()
        time.sleep(5)  # page transition

        self.driver.find_element_by_xpath(
            '//*[@id="layer_cart"]/div[1]/div[1]/span').click()
        time.sleep(3)  # page transition
        text_cart = self.driver.find_element_by_xpath(
            '//*[@id="product_4_16_0_307768"]/td[2]/p/a').text

        assert "Added in cart" in text_cart

    @flaky
    @pytest.mark.my_account
    @pytest.mark.functional_suite
    def test_delete_item_from_cart(self):
        self.driver.get(self.html_address_main_page)

        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div[3]/div/div/div[3]/div/a').click()
        time.sleep(3)  # page transition
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="5_19_0_307768"]/i').click()
            assert True
        except:
            assert False, "Item was not removed from the cart"

    @flaky
    @pytest.mark.my_account
    @pytest.mark.functional_suite
    def test_verify_cart(self):
        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div[3]/div/div/div[3]/div/a').click()
        time.sleep(3)  # page transition
        emtpy_cart_text = self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/p').text
        assert emtpy_cart_text == "Your shopping cart is empty.", "Cart is not empty"

    @flaky
    @pytest.mark.my_account
    @pytest.mark.functional_suite
    def test_logout_user(self):
        self.driver.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div/nav/div[2]/a').click()
        time.sleep(2)  # page transition
        assert self.driver.title == "My account - My Store"

    @flaky
    @pytest.mark.main_page
    @pytest.mark.functional_suite
    def test_newsletter_email(self):
        self.driver.get(self.html_address_main_page)
        email_area = self.driver.find_element_by_id('newsletter-input')
        email_area.send_keys("qwerty123@yahoo.com")
        self.driver.find_element_by_xpath(
            '//*[@id="newsletter_block_left"]/div/form/div/button').click()
        text = self.driver.find_element_by_xpath(
            '//*[@id="columns"]/p').text
        time.sleep(2)  # page transition
        assert text == "Newsletter : You have successfully subscribed to this newsletter."

    @flaky
    @pytest.mark.main_page
    @pytest.mark.functional_suite
    @pytest.mark.parametrize("search_item", ["dress", "printed", "abc", "invalid", "skirt", "shirt", "evening", "summer", "casuall"])
    def test_search_item(self, search_item):
        self.driver.get(self.html_address_main_page)
        search_area = self.driver.find_element_by_id('search_query_top')
        search_area.send_keys(search_item)
        self.driver.find_element_by_xpath(
            '//*[@id="searchbox"]/button').submit()
        time.sleep(2)  # page transition
        app_text = self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/h1').text
        assert search_item.upper() in app_text

    @flaky
    @pytest.mark.main_page
    @pytest.mark.functional_suite
    def test_page_contact(self):
        self.driver.get(self.html_address_main_page)
        self.driver.find_element_by_xpath('//*[@id="contact-link"]/a').click()
        time.sleep(3)  # page transition
        assert self.driver.title == "Contact - My Store"

    @flaky
    @pytest.mark.main_page
    @pytest.mark.functional_suite
    def test_terms_and_conditions(self):
        self.driver.get(self.html_address_main_page)
        self.driver.find_element_by_xpath(
            '//*[@id="block_various_links_footer"]/ul/li[6]/a').click()
        time.sleep(3)  # page transition
        assert "Terms and conditions of use" in self.driver.title

    @flaky
    @pytest.mark.parametrize("item_name,item_xpath", [("Facebook", '//*[@id="social_block"]/ul/li[1]/a'),
                                                      ("Tweeter",
                                                       '//*[@id="social_block"]/ul/li[2]/a'),
                                                      ("Youtube",
                                                       '//*[@id="social_block"]/ul/li[3]/a'),
                                                      ("Google",
                                                       '//*[@id="social_block"]/ul/li[4]/a'),
                                                      ("Instagram",
                                                       '//*[@id="social_block"]/ul/li[5]/a')])
    @pytest.mark.main_page
    @pytest.mark.functional_suite
    def test_follow_us(self, item_name, item_xpath):
        self.driver.get(self.html_address_main_page)
        self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)  # page transition
        try:
            element = self.driver.find_element_by_xpath(item_xpath)
            assert element.is_displayed(), (item_name, "is not displayed")
        except Exception:
            assert False, (item_name, "is not displayed")
