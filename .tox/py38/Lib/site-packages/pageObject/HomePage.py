from selenium.webdriver.common.by import By
from pageObject.AppsPage import AppsPage
from pageObject.ExplorePage import ExplorePage
from pageObject.PricePage import PricePage
from pageObject.TipsPage import TipsPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    logo = (By.CSS_SELECTOR, "[class='logo__image']")
    search = (By.CSS_SELECTOR, "[name='search']")
    apps = (By.XPATH,
            "//span[@class='navigation-links-v2__inner-link navigation-links-v2__inner-link--selectable'][contains(text(),'Apps')]")
    explore = (By.XPATH,
               "//span[@class='navigation-links-v2__inner-link navigation-links-v2__inner-link--selectable'][contains(text(),'Explore')]")
    tips = (By.XPATH,
            "//span[@class='navigation-links-v2__inner-link navigation-links-v2__inner-link--selectable'][contains(text(),'Tips & Advice')]")
    price = (By.XPATH,
             "//span[@class='navigation-links-v2__inner-link navigation-links-v2__inner-link--selectable'][contains(text(),'Pricing')]")

    def get_logo(self):
        return self.driver.find_element(*HomePage.logo)

    def get_searchBar(self):
        return self.driver.find_element(*HomePage.search)

    def goto_Apps(self):
        self.driver.find_element(*HomePage.apps).click()
        apps_page = AppsPage(self.driver)
        return apps_page

    def goto_Explore(self):
        self.driver.find_element(*HomePage.explore).click()
        explore_page = ExplorePage(self.driver)
        return explore_page

    def goto_TipsAndAdvice(self):
        self.driver.find_element(*HomePage.tips).click()
        tips_page = TipsPage(self.driver)
        return tips_page

    def goto_Pricing(self):
        self.driver.find_element(*HomePage.price).click()
        price_page = PricePage(self.driver)
        return price_page
