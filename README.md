# DemoHRMPlaywrightDemo

Playwright + pytest test suite for the [OrangeHRM Live demo](https://opensource-demo.orangehrmlive.com/) — an open-source HR management system. The suite covers Web UI interactions via the Page Object Model and is prepared to grow with REST API tests.

## What it does

- Automates browser-based tests against the OrangeHRM Live demo site
- Follows the **Page Object Model** pattern to keep test logic separate from UI interaction details
- Generates HTML reports via `pytest-html`
- Supports test data generation with `faker` and environment configuration with `python-dotenv`

## Project structure

```
DemoHRMPlaywrightDemo/
├── web_ui/               # Page Object classes
│   ├── user_page.py      # UserPage — base class (side menu, page summary)
│   ├── login_page.py     # LoginPage — login screen operations
│   └── dashboard_page.py # DashboardPage — post-login dashboard
├── rest_api/             # REST API client classes (placeholder)
├── fixtures/             # Shared pytest fixtures
│   └── web_ui.py         # Web UI fixtures (e.g. login_page)
├── tests/
│   ├── web_ui/           # Web UI tests
│   └── rest_api/         # REST API tests
└── pyproject.toml        # Project metadata and dependencies
```

## Setup

**Prerequisites:** Python 3.14+, [uv](https://docs.astral.sh/uv/)

```bash
# Install dependencies
uv sync

# Install Playwright browsers
uv run playwright install
```

## Running tests

```bash
# Run all tests (HTML report saved to reports/report.html)
uv run pytest

# Run only Web UI tests
uv run pytest tests/web_ui/

# Run a specific test file
uv run pytest tests/web_ui/test_login.py

# Run in headed mode (visible browser)
uv run pytest --headed

# Run against a specific browser
uv run pytest --browser firefox
```

## Generating test cases with the Claude agent

You can ask the Claude agent to generate a fully working pytest test by describing your test case in the structured format below.

### Prompt template

```
Create a test case for <WebUI|REST API>:
Test Case Name: <short name that describes what is being verified>
Test Case Description: <one sentence — what the test proves>
Steps:
Given <initial state or precondition>
When <action performed by the user or system>
Then <expected outcome>
And <additional assertion, if needed>
```

> Use `WebUI` for browser tests and `REST API` for HTTP-level tests.  
> Each step goes on its own line. Add as many `And` lines as needed.

### Fields

| Field | Maps to | Rules |
|---|---|---|
| **Test Case Name** | Python function name (`test_<snake_case>`) | Short, descriptive, starts with a verb |
| **Test Case Description** | Function docstring (first line) | One complete sentence |
| **Steps** | Test body assertions and actions | Gherkin keywords: `Given`, `When`, `Then`, `And` |

### Gherkin keywords

| Keyword | Purpose |
|---|---|
| `Given` | Sets up the precondition or initial state |
| `When` | Describes the action being tested |
| `Then` | States the expected outcome |
| `And` | Continues the previous step with an additional condition |

### Example

```
Create a test case for WebUI:
Test Case Name: Verify if user can be logged in with correct credentials
Test Case Description: User enters correct credentials and is redirected into Dashboard page
Steps:
Given user logins with username Admin and password admin123
When user is really logged in
Then user is on the page named Dashboard
And all side menu links are present
```

### What Claude generates

- A test function placed in `tests/web_ui/` or `tests/rest_api/` depending on the type
- Docstring built from the description and the Gherkin steps
- Test body derived step-by-step from the steps, using existing Page Object methods and fixtures
- No duplicate code — Claude reads the `web_ui` package and `fixtures` before writing anything

### Tips

- The more precise your Gherkin steps, the more accurate the generated test
- If a page object method or fixture needed for the test does not exist yet, ask Claude to create it first
