import pytest
import selenium
from common_files.test_web_driver import TestBrowser


@pytest.mark.usefixtures("driver_init")
class TestSuiteUI(TestBrowser):
    html_address_main_page = "http://automationpractice.com/"

    @pytest.mark.main_page
    @pytest.mark.user_interface_suite
    def test_main_page_initialization(self):
        self.driver.get(self.html_address_main_page)
        assert self.driver.title == "My Store"

    @pytest.mark.main_page
    @pytest.mark.user_interface_suite
    @pytest.mark.parametrize("item_name,item_xpath", [("Woman", '//*[@id = "block_top_menu"]/ul/li[1]/a'),
                                                      ("Dresses",
                                                       '//*[@id="block_top_menu"]/ul/li[2]/a'),
                                                      ("T-Shirt",
                                                       '//*[@id="block_top_menu"]/ul/li[3]/a'),
                                                      ("Search",
                                                       '//*[@id="search_query_top"]'),
                                                      ("Cart",
                                                       '//*[@id="header"]/div[3]/div/div/div[3]/div/a/b'),
                                                      ("Contact us",
                                                       '//*[@id="contact-link"]/a'),
                                                      ("Sign In",
                                                       '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'),
                                                      ("About", '//*[@id="header"]/div/nav/div[1]/a')])
    def test_element_is_shown(self, item_name, item_xpath):
        try:
            self.driver.find_element_by_xpath(item_xpath)
            value_found = True
        except Exception:
            value_found = False
        assert value_found == True, (item_name, "item was not found.")

    @pytest.mark.main_page
    @pytest.mark.user_interface_suite
    @pytest.mark.parametrize("item_size,item_xpath", [("18px", '//*[@id = "block_top_menu"]/ul/li[1]/a'),
                                                      ("18px",
                                                       '//*[@id="block_top_menu"]/ul/li[2]/a'),
                                                      ("18px",
                                                       '//*[@id="block_top_menu"]/ul/li[3]/a'),
                                                      ("13px",
                                                       '//*[@id="search_query_top"]'),
                                                      ("13px",
                                                       '//*[@id="header"]/div[3]/div/div/div[3]/div/a/b'),
                                                      ("13px",
                                                       '//*[@id="contact-link"]/a'),
                                                      ("13px",
                                                       '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')])
    def test_text_size(self, item_size, item_xpath):
        size_text = self.driver.find_element_by_xpath(
            item_xpath).value_of_css_property("font-size")
        assert size_text == item_size, ("Size is not correct for:", item_xpath)

    @pytest.mark.main_page
    @pytest.mark.user_interface_suite
    @pytest.mark.parametrize("item_color,item_xpath", [("rgba(72, 72, 72, 1)", '//*[@id = "block_top_menu"]/ul/li[1]/a'),
                                                       ("rgba(72, 72, 72, 1)",
                                                        '//*[@id="block_top_menu"]/ul/li[2]/a'),
                                                       ("rgba(72, 72, 72, 1)",
                                                        '//*[@id="block_top_menu"]/ul/li[3]/a'),
                                                       ("rgba(156, 155, 155, 1)",
                                                        '//*[@id="search_query_top"]'),
                                                       ("rgba(255, 255, 255, 1)",
                                                        '//*[@id="header"]/div[3]/div/div/div[3]/div/a/b'),
                                                       ("rgba(156, 155, 155, 1)",
                                                        '//*[@id="contact-link"]/a'),
                                                       ("rgba(255, 255, 255, 1)",
                                                        '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')])
    def test_text_color(self, item_color, item_xpath):
        size_text = self.driver.find_element_by_xpath(
            item_xpath).value_of_css_property("color")
        assert size_text == item_color, (
            "Color is not correct for:", item_xpath)

    @pytest.mark.main_page
    @pytest.mark.user_interface_suite
    def test_change_window_size(self):
        self.driver.set_window_size(500, 500)
        values = self.driver.get_window_size()
        assert values['height'] == 500 and values['width'] == 500
