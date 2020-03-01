import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.config import Config


driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run test: dev, qa or uat",
        default="test"
    )
    parser.addoption(
        "--browser",
        action="store",
        help="Browser in which test is ran: chrome, firefox or ie",
        default="chrome"
    )


@pytest.fixture(scope='class')
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='class')
def app_config(env):
    cfg = Config(env)
    return cfg


@pytest.fixture(scope="function")
def setup(request, app_config):
    global driver
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(app_config.base_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
