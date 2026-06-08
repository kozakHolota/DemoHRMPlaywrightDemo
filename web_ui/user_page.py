from playwright.sync_api import Page, Locator


class UserPage:
    def __init__(self, page: Page, page_name: str) -> None:
        self.page = page
        self.page_name = page_name

    def __get_side_menu_item(self, name: str):
        """Get button on the side menu by it's name"""
        return self.page.get_by_role("link", name=name)

    @property
    def page_summary(self) -> Locator:
        """Returns the summary of the page"""
        return self.page.locator(".oxd-topbar-header-breadcrumb-module", has_text=self.page_name)

    @property
    def admin_menu(self) -> Locator:
        """Returns the admin menu"""
        return self.__get_side_menu_item("Admin")

    @property
    def pim_menu(self) -> Locator:
        """Returns the pim menu"""
        return self.__get_side_menu_item("PIM")

    @property
    def leave_menu(self) -> Locator:
        """Returns the leave menu"""
        return self.__get_side_menu_item("Leave")

    @property
    def time_menu(self) -> Locator:
        """Returns the time menu"""
        return self.__get_side_menu_item("Time")

    @property
    def recruitment_menu(self) -> Locator:
        """Returns the recruitment menu"""
        return self.__get_side_menu_item("Recruitment")

    @property
    def my_info_menu(self) -> Locator:
        """Returns the my info menu"""
        return self.__get_side_menu_item("My Info")

    @property
    def performance_menu(self) -> Locator:
        """Returns the performance menu"""
        return self.__get_side_menu_item("Performance")

    @property
    def dashboard_menu(self) -> Locator:
        """Returns the dashboard menu"""
        return self.__get_side_menu_item("Dashboard")

    @property
    def directory_menu(self) -> Locator:
        """Returns the directory menu"""
        return self.__get_side_menu_item("Directory")

    @property
    def maintenance_menu(self) -> Locator:
        """Returns the maintenance menu"""
        return self.__get_side_menu_item("Maintenance")

    @property
    def claim_menu(self) -> Locator:
        """Returns the claim menu"""
        return self.__get_side_menu_item("Claim")

    def check_side_menu(self) -> bool:
        """Returns True if all side menu items are visible"""
        return (
            self.admin_menu.is_visible() and
            self.pim_menu.is_visible() and
            self.leave_menu.is_visible() and
            self.time_menu.is_visible() and
            self.recruitment_menu.is_visible() and
            self.my_info_menu.is_visible() and
            self.performance_menu.is_visible() and
            self.dashboard_menu.is_visible() and
            self.directory_menu.is_visible() and
            self.maintenance_menu.is_visible() and
            self.claim_menu.is_visible()
        )
