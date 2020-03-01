from selenium.webdriver.common.by import By


class PricePage:

    def __init__(self, driver):
        self.driver = driver

    pricingContent = (By.CSS_SELECTOR, "[class='css-ci2sxl-PricingPage__wrapper']")

    def check_pricingContent(self):
        return self.driver.find_elements(*PricePage.pricingContent)
