from selenium.webdriver.common.by import By


class AppsPage:

    def __init__(self, driver):
        self.driver = driver

    appsSideBar = (By.CSS_SELECTOR, "[class='css-1s83mnu-ExploreLayout__sidebar']")
    appsContent = (By.CSS_SELECTOR, "[class='css-hfne9l-ExploreLayout__content']")
    appsTopBar = (By.CSS_SELECTOR, "[class='css-1qwtxwm-UniversalTopbar--medium']")

    def check_sideBar(self):
        return self.driver.find_elements(*AppsPage.appsSideBar)

    def check_mainContent(self):
        return self.driver.find_elements(*AppsPage.appsContent)

    def check_topBar(self):
        return self.driver.find_element(*AppsPage.appsTopBar)
