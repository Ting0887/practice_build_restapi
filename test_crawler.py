import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestWealthCrawler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--log-level=1")
        chrome_options.add_argument("--disable-3d-apis")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('blink-settings=imagesEnabled=false')
        chrome_options.add_argument("--disable-javascript")
        chrome_options.add_argument("--disable-images")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--disable-plugins")
        chrome_options.add_argument("--in-process-plugins")
        
        service = Service(ChromeDriverManager().install())
        cls.browser = webdriver.Chrome(service=service, options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_page_load(self):
        url = 'https://www.wealth.com.tw/lists/categories/2c6379e9-7527-442b-880a-bb9552689e06'
        self.browser.get(url)
        time.sleep(2)
        self.assertIn("財訊", self.browser.title)

    def test_button_click(self):
        url = 'https://www.wealth.com.tw/lists/categories/2c6379e9-7527-442b-880a-bb9552689e06'
        self.browser.get(url)
        time.sleep(2)

        # Click "我知道了" button
        try:
            button = self.browser.find_element(By.XPATH, '//button[text()="我知道了"]')
            button.click()
        except Exception as e:
            print(f"Exception occurred while clicking '我知道了' button: {e}")

        # Click "想看更多" button
        try:
            more_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="想看更多"]'))
            )
            more_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"Exception occurred while clicking '想看更多' button: {e}")

    def test_content_extraction(self):
        url = 'https://www.wealth.com.tw/articles/ca791c2e-0a67-4c2f-a611-99694c60521e'
        self.browser.get(url)
        time.sleep(2)
        soup = BeautifulSoup(self.browser.page_source, 'lxml')

        def extract_content(soup):
            content = []
            try:
                contents = soup.find_all('p', 'qdr-paragraph')
                for c in contents:
                    text = c.get_text()
                    cleaned_text = text.replace('\ufeff', '').strip()  # 去除 \ufeff 和首尾空白字符
                    content.append(cleaned_text)
            except AttributeError as e:
                print(f"An error occurred: {e}")
            return '\n'.join(content)

        content = extract_content(soup)
        self.assertTrue(len(content) > 0)
    
    def test_title_extraction(self):
        url = "https://www.wealth.com.tw/lists/categories/2c6379e9-7527-442b-880a-bb9552689e06"
        self.browser.get(url)
        time.sleep(2)
        soup = BeautifulSoup(self.browser.page_source, 'lxml')

        def extract_title(soup):
            try:
                return soup.find('h2').text
            except AttributeError:
                return ''
        title = extract_title(soup)
        self.assertTrue(len(title) > 0)

if __name__ == '__main__':
    unittest.main()