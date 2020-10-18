import regex as re
import time
import os
from adnar_scraper import settings
from random import randint

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from fake_useragent import UserAgent


class SeleniumController:
    def __init__(self):
        #fallback='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        ua = UserAgent()

        print("User Agent Loaded")

        self.user_agent_list = []

        for i in range(10000):
            self.user_agent_list.append(ua.random)

    def get_ghost_driver(self):
        user_agent = self.user_agent_list[randint(0, 9999)]

        options = Options()

        options.add_argument("start-maximized")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-browser-side-navigation")
        options.add_argument("enable-automation")
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--dns-prefetch-disable")
        options.add_argument("--disable-gpu")
        options.add_argument(f'user-agent={user_agent}')

        if os.name == 'nt':
            # If Windows
            chrome_driver_file = "chromedriver.exe"
        else:
            # If Linux
            chrome_driver_file = "chromedriver"

        driver = webdriver.Chrome(settings.UTILITY_DATABASE_PATH + 'driver/' + chrome_driver_file, options=options)

        return driver

    @staticmethod
    def print_percent(full_item_length, data_len_list):
        count = 0

        for length in data_len_list :
            count += length

        print(str(count / full_item_length * 100) + '%')

    def get_tag_in_new_tab(self, driver, item_url):
        # Switch to new tab
        driver.execute_script("window.open('')")
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        driver.switch_to_window(driver.window_handles[-1])
        driver.get(item_url)

        # Get Tags
        tags = []

        try:
            tag_list = driver.find_elements_by_xpath('//div[contains(@class, "goods_tag")]/ul/li/a')

            for tag_item in tag_list:
                tags.append(re.sub(pattern="#", repl="", string=tag_item.text))

            if len(tags) == 0:
                self.get_to_bottom(driver=driver, scroll_pause_time=0.1)

                tag_list = driver.find_elements_by_xpath('//li[contains(@class, "itm.tag")]/a')

                for tag_item in tag_list:
                    tags.append(re.sub(pattern="#", repl="", string=tag_item.text))

        except Exception as e:
            print(e)

        # Switch focus to old tab and close opened tab
        driver.close()
        driver.switch_to_window(driver.window_handles[0])

        return tags

    @staticmethod
    def get_to_bottom(driver, scroll_pause_time):
        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

