from pytest import mark
from Utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage


@mark.smoke
class SmokeTests(BaseClass):

    def test_goto_apps(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        apps_page = homepage.goto_Apps()
        log.info("Navigate to Apps Page")
        apps_content = apps_page.check_mainContent()
        log.info("Smoke Test Apps Main Content Section")
        assert apps_content is not None

    def test_goto_explore(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        explore_page = homepage.goto_Explore()
        log.info("Navigate to Explore Page")
        explore_content = explore_page.check_popularArticles()
        log.info("Smoke Test Popular Articles")
        assert explore_content is not None

    def test_goto_tips(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        tip_page = homepage.goto_TipsAndAdvice()
        log.info("Navigate to Tips & Advice Page")
        tip_content = tip_page.check_tipsSubscription()
        log.info("Smoke Test Subscription")
        assert tip_content is not None

    def test_goto_pricing(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        price_page = homepage.goto_Pricing()
        log.info("Navigate to Pricing Page")
        price_content = price_page.check_pricingContent()
        log.info("Smoke Test Main Price Content Section")
        assert price_content is not None
