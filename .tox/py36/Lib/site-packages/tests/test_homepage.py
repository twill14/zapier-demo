from pytest import mark
from Utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from pageObject.AppsPage import AppsPage

@mark.home
class HomePageTests(BaseClass):

    def test_logo(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Checking Logo is Present")
        img_source = homepage.get_logo().get_attribute("src")
        assert "https://cdn.zapier.com/ssr/1a57f1f796c1fd66a1380ee168dfb612ce7e21f1/_next/static/images/zapier-small-orange-logo.png" in img_source

    def test_search_bar(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Checking Search bar is present")
        search_bar = homepage.get_searchBar()
        assert search_bar is not None
