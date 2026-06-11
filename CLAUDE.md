# DemoHRMPlaywrightDemo

Playwright + pytest test suite for the [OrangeHRM Live demo](https://opensource-demo.orangehrmlive.com/).

## Project structure

```
DemoHRMPlaywrightDemo/
├── web_ui/               # Web Page Object classes (Page Object Model)
│   ├── user_page.py      # UserPage — base class for all page objects
│   ├── login_page.py     # LoginPage — login screen operations
│   └── dashboard_page.py # DashboardPage — post-login dashboard
├── rest_api/             # REST API client classes (placeholder, not yet implemented)
├── fixtures/             # pytest fixtures shared across test suites
│   └── web_ui.py         # Web UI fixtures (e.g. login_page)
├── tests/
│   ├── web_ui/           # Web UI tests — place all new Web UI tests here
│   └── rest_api/         # REST API tests — place all new REST API tests here
└── pyproject.toml        # Project metadata and dependencies
```
## Writing tests from Claude agent prompt

Use the `/generate-test` skill (`.claude/skills/generate-test.md`) to generate tests.

Provide:
- **Test case name** — becomes the `test_` function name
- **Test case description** — becomes the docstring
- **Test case steps** — in Gherkin format (`Given / When / Then / And`), one per line

## Writing Web UI tests

- All Web UI tests go into `tests/web_ui/`.
- Page objects live in the `web_ui` package. Before writing a test, search the classes and methods in that package and use their docstrings to understand available operations and return types.
- Key classes:
  - `web_ui.login_page.LoginPage` — entry point; use `login()` to authenticate and receive a `DashboardPage` or `LoginPage` back.
  - `web_ui.dashboard_page.DashboardPage` — post-login page; inherits `UserPage`.
  - `web_ui.user_page.UserPage` — base class; provides side-menu locators and `check_side_menu()`.
- Use `pytest-playwright`; fixtures provide a `page: Page` argument.
- Reusable pytest fixtures are defined in the `fixtures` package. Before creating a new fixture, check existing ones:
  - `fixtures.web_ui.login_page` — returns a `LoginPage` instance ready to use.

## Writing REST API tests

- All REST API tests go into `tests/rest_api/`.
- REST API client classes live in the `rest_api` package. Before writing a test, search the classes and methods in that package and use their docstrings to understand available operations and return types.
- The `rest_api` package is currently a placeholder; add client modules there as the suite grows.

## Dependencies

| Package | Purpose |
|---|---|
| playwright / pytest-playwright | Browser automation |
| pytest | Test runner |
| pytest-asyncio | Async test support |
| allure-pytest | Test reporting |
| python-dotenv | Environment variable management |
| faker | Test data generation |
