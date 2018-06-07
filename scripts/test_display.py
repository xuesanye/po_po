import os,sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.display_page import DisplayPage

class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    def test_mobile_display_input(self):

        self.display_page.click_search()
        self.display_page.input_search_text('hello')
        self.display_page.click_back()


        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()

    def teardown(self):
        self.driver.quit()
