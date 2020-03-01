from selenium.webdriver.common.by import By


class ExplorePage:

    def __init__(self, driver):
        self.driver = driver

    explorePopArticles = (By.CSS_SELECTOR, "[class='popular-articles-wrapper']")
    exploreAppGrid = (By.CSS_SELECTOR, "[class='ReactVirtualized__Grid service-picker__apps-list']")

    def check_popularArticles(self):
        return self.driver.find_elements(*ExplorePage.explorePopArticles)

    def check_appGrid(self):
        return self.driver.find_elements(*ExplorePage.exploreAppGrid)
