from playwright.sync_api import Page

from web_ui.user_page import UserPage


class DashboardPage(UserPage):
    def __init__(self, page: Page):
        super().__init__(page, "Dashboard")

    @property
    def is_logged_in(self):
        """Shows if user is logged in"""
        return True