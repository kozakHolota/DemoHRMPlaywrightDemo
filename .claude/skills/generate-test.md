---
name: generate-test
description: Generate a Playwright pytest test from a structured test case description
---

You are generating a test for the DemoHRMPlaywrightDemo project — a Playwright + pytest suite for OrangeHRM Live.

## Input format

The user must provide:
1. **Test case name** — becomes the test function name (snake_case, prefixed with `test_`)
2. **Test case description** — becomes the docstring (include the Gherkin steps verbatim)
3. **Test case steps** — in Gherkin format (Given / When / Then / And), one per line

If any of these are missing, ask for them before generating code.

## Before writing code

1. Read all page object classes in `web_ui/` and their docstrings to know what methods and properties are available.
2. Check `fixtures/web_ui.py` for available fixtures.
3. Check `tests/web_ui/conftest.py` to confirm which fixtures are already imported there.

## Generation rules

### File placement
- Web UI tests → `tests/web_ui/test_<name>.py`
- REST API tests → `tests/rest_api/test_<name>.py`
- If a suitable test file already exists, append the function to it instead of creating a new file.

### Test function structure
```python
def test_<name>(<fixtures>):
    """<description>

    <Gherkin steps verbatim>
    """
    # test body
```

### Fixtures
- Use `login_page` fixture (from `fixtures.web_ui`) to get a `LoginPage` instance.
- `conftest.py` in `tests/web_ui/` already does `from fixtures.web_ui import *` — do NOT re-import fixtures inside the test file unless conftest is missing them.
- Never inject `page: Page` directly unless the test explicitly needs raw page access.

### Assertions
- Map each **Then** / **And** step to an explicit `assert` with a descriptive failure message.
- Use `playwright`'s `expect()` for visibility/state checks when appropriate.
- Prefer page-object properties over raw locators inside tests.

### No extra imports
- Only import what the test body actually uses.
- Do not import `pytest` unless the test uses markers or `pytest.raises`.

### Style
- No inline comments unless a step's intent is non-obvious.
- One blank line between logical sections (arrange / act / assert).
- Follow the pattern in `tests/web_ui/test_login.py` as the canonical example.

## Available page objects (summary)

| Class | Module | Key members |
|---|---|---|
| `LoginPage` | `web_ui.login_page` | `login(username, password) → DashboardPage\|LoginPage`, `is_logged_in`, `incorrect_credential_label` |
| `DashboardPage` | `web_ui.dashboard_page` | `is_logged_in`, inherits `UserPage` |
| `UserPage` | `web_ui.user_page` | `page_summary`, `check_side_menu()`, `admin_menu`, `pim_menu`, `leave_menu`, `time_menu`, `recruitment_menu`, `my_info_menu`, `performance_menu`, `dashboard_menu`, `directory_menu`, `maintenance_menu`, `claim_menu` |

## After generating

1. Show the complete file content (or the appended function if adding to an existing file).
2. Write the file to disk.
3. Run `python -m pytest <test_file_path> -v` and report the result.
