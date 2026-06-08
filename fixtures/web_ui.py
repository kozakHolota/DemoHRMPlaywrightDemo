import base64

from playwright.sync_api import Page
from pytest import fixture, hookimpl
from pytest_html import extras

from web_ui.login_page import LoginPage


@hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if call.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page is not None:
            try:
                page.wait_for_load_state("networkidle", timeout=10_000)
            except Exception:
                pass
            screenshot = base64.b64encode(page.screenshot()).decode("utf-8")
            rep.extras = getattr(rep, "extras", [])
            rep.extras.append(extras.image(screenshot, mime_type="image/png"))


@fixture
def login_page(page: Page):
    page.set_default_timeout(10_000)
    return LoginPage(page)