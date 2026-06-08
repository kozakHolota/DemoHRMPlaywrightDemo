from fixtures.web_ui import login_page  # noqa: F401


def test_login_with_correct_credentials(login_page):
    """User enters correct credentials and is redirected into Dashboard page.

    Given user logins with username Admin and password admin123
    When user is really logged in
    Then user is on the page named Dashboard
    And all side menu links are present
    """
    dashboard_page = login_page.login("Admin", "admin123")

    assert dashboard_page.is_logged_in, "User is not logged in"
    assert dashboard_page.page_name == "Dashboard", "Page name is not Dashboard"
    assert dashboard_page.check_side_menu(), "Not all side menu links are present"
