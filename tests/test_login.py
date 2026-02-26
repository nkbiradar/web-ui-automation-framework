import pytest
from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.parametrize("username,password,expected_result", [
    ("standard_user", "secret_sauce", "success"),
    ("invalid_user", "wrong_password", "failure"),
])
def test_login(driver, username, password, expected_result):
    logger.info(f"Executing login test with username: {username}")

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)

    if expected_result == "success":
        logger.info("Verifying successful login")
        assert "inventory.html" in driver.current_url
    else:
        logger.info("Verifying failed login")
        assert "Username and password do not match" in login_page.get_error_message()