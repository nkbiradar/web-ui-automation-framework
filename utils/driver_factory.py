from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.settings import BROWSER


def get_driver():
    browser = BROWSER.lower()

    if browser == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")

        # Headless support (important for CI)
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    else:
        raise Exception(f"Browser '{browser}' is not supported!")

    driver.implicitly_wait(5)
    return driver