import pytest
from bs4 import BeautifulSoup


def _get_token(html_source: str) -> str:
    """Returns the token from the HTML source."""
    soup = BeautifulSoup(html_source, "html.parser")

    auth_login = soup.select_one("auth-login")
    token = auth_login[":token"]

    return str(token).replace("&quot;", "").strip('"')

@pytest.fixture(scope="session")
def api_context(playwright):
    token = _get_token(playwright.request.get("https://opensource-demo.orangehrmlive.com").text)
    context = playwright.request.new_context(
        base_url="https://opensource-demo.orangehrmlive.com",
    )
    yield context
    context.dispose()