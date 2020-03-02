from selenium.webdriver.common.by import By


class TipsPage:

    def __init__(self, driver):
        self.driver = driver

    tipsSubscription = (By.CSS_SELECTOR, "[class='row blog-subscribe']")
    blogCategories = (By.CSS_SELECTOR, "[class='blog-cats']")

    def check_tipsSubscription(self):
        return self.driver.find_elements(*TipsPage.tipsSubscription)

    def check_blogCategories(self):
        return self.driver.find_elements(*TipsPage.blogCategories)
