from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class TestArticle():

    def basic_element_test(self):
        baseUrl = "https://www.gobankingrates.com/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        # Open an article example
        test_article = driver.find_element(By.LINK_TEXT, "10 Best Savings Accounts of 2019")
        test_article.click()

        # Title verification
        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains("10 Best Savings Accounts of 2019"))

        title = driver.title
        print('Title is: ' + title)



ff = TestArticle()
ff.basic_element_test()