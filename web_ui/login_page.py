from playwright.sync_api import Page, Locator, expect

from web_ui.dashboard_page import DashboardPage


class LoginPage:
    """Page object for login page. Operations:
    - Login operation
    - property is_logged_in
    """
    def __init__(self, page: Page):
        self.page = page
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    @property
    def is_logged_in(self) -> bool:
        """Shows if user is logged in"""
        return False

    @property
    def incorrect_credential_label(self) -> Locator:
        """Label for incorrect credentials"""
        return self.page.get_by_text("Invalid credentials")

    def login(self, username: str, password: str) -> DashboardPage | LoginPage:
        """Login to orangehr-live.
        Args:
            username (str): username
            password (str): password

        Returns:
            DashboardPage: DashboardPage object if page summary 'Dashboard' exists else LoginPage
        """
        self.page.fill("[name='username']", username)
        self.page.fill("[name='password']", password)
        self.page.locator("[type=submit]").click()

        dashboard_page = DashboardPage(self.page)

        try:
            expect(dashboard_page.page_summary).to_be_visible(timeout=10_000)
            return dashboard_page
        except Exception:
            return self

