import os,sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.network_page import NetWorkPage

class TestNetwork:

    def setup(self):
        self.driver = init_driver()
        self.network_page = NetWorkPage(self.driver)

    def test_mobile_network_2g(self):

        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.click_2g()


    def test_mobile_network_3g(self):

        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.click_3g()


    def teardown(self):
        self.driver.quit()
