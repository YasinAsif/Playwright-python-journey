# Playwright Python Journey

A structured, day-by-day repository documenting my mastery of end-to-end test automation using Playwright and Python — built the SDET way.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Playwright](https://img.shields.io/badge/Playwright-1.40+-2EAD33?logo=playwright&logoColor=white)](https://playwright.dev)
[![pytest](https://img.shields.io/badge/pytest-8.x-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/YasinAsif/Playwright-python-journey?style=social)](https://github.com/YasinAsif/Playwright-python-journey/stargazers)

## Journey Progress

| Day   | Topic                                              | Status          |
|-------|----------------------------------------------------|-----------------|
| Day 1 | Playwright Fundamentals — Navigation & Assertions  | Complete        |
| Day 2 | Locators & Selectors — Semantic & Resilient        | Coming Soon     |
| Day 3+| …more to come                                      | Locked          |

## Day 1 — Playwright Fundamentals

**File:** `Day1/test_playwright.py`

Day 1 focuses on the core building blocks of Playwright: launching a browser, navigating to a URL, and writing production-grade assertions  exactly what you'd ship in a real SDET role.

### Tests Written

| Test                     | What It Verifies                          | API Used                          |
|--------------------------|-------------------------------------------|-----------------------------------|
| test_verify_page_url     | Page navigates to the correct URL         | expect(page).to_have_url()        |
| test_verify_page_title   | Page title matches expected value         | expect(page).to_have_title()      |

### Key Concepts

```python
from playwright.sync_api import Page, expect

def test_verify_page_url(page: Page):
    """Verify that navigating to Automation Exercise returns the correct URL."""
    page.goto("https://automationexercise.com/")
    expect(page).to_have_url("https://automationexercise.com/")


def test_verify_page_title(page: Page):
    """Verify that the Automation Exercise homepage has the correct title."""
    page.goto("https://automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")
```

### Run Day 1 Tests

```bash
# Run with project defaults (headed, slow-mo, verbose)
python -m pytest Day1/

# Run headless (ideal for CI)
python -m pytest Day1/ --headless

# Run a specific test
python -m pytest Day1/test_playwright.py::test_verify_page_url
```

### Passing Output Example

```bash
============================= test session starts ==============================
platform win32 -- Python 3.11.9
collected 2 items

Day1/test_playwright.py::test_verify_page_url   PASSED  [ 50%]
Day1/test_playwright.py::test_verify_page_title PASSED  [100%]

============================== 2 passed in ~7s ================================
```

## Day 2 — Coming Soon

**Locators & Selectors: The SDET Way**

Deep dive into Playwright's semantic locators (get_by_role, get_by_label, get_by_placeholder, get_by_text, get_by_test_id).
Brittle CSS/XPath selectors have no place in a production test suite.

## Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/YasinAsif/Playwright-python-journey.git
   cd Playwright-python-journey
   ```

2. **Create & activate virtual environment**
   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # macOS / Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

4. **Run the tests**
   ```bash
   python -m pytest Day1/
   ```

## Tech Stack

| Tool              | Version   | Purpose                              |
|-------------------|-----------|--------------------------------------|
| Python            | 3.11+     | Core language                        |
| Playwright        | ≥ 1.40    | Browser automation engine            |
| pytest            | ≥ 8.x     | Test runner & reporting              |
| pytest-playwright | ≥ 0.4     | Playwright + pytest integration      |

## Project Structure

```plaintext
Playwright-python-journey/
├── Day1/
│   └── test_playwright.py          # Navigation & assertions
├── conftest.py                     # Shared pytest fixtures
├── pytest.ini                      # Pytest + Playwright config
├── requirements.txt                # Python dependencies
└── .gitignore
```

## Author

**Yasin Asif** — Learning in public. Building toward SDET mastery, one commit at a time.

Star the repo if you're on the same journey!
Pull requests, issues, and suggestions are always welcome.
