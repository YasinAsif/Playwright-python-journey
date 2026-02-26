# 🎭 Playwright SDET QA Portfolio

A structured learning repository documenting my journey mastering **end-to-end test automation** with [Playwright](https://playwright.dev/) and Python.

---

## 🗂️ Project Structure

```
Playwright-SDET QA/
│
├── Day1/                          # Fundamentals: Navigation & Assertions
│   └── test_playwright.py
│
├── practice play-wright/          # Standalone scripts for hands-on practice
│   ├── practice- browser launch.py   # Browser launch, screenshot, title
│   └── Locators/
│       └── 01_get_by_role.py     # get_by_role locator demo on SauceDemo
│
├── Playwright-practice1.py        # First script: navigate & print title
├── conftest.py                    # Shared pytest fixtures (future use)
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # Python dependencies
└── .gitignore                     # Files excluded from version control
```

---

## 📅 Day-by-Day Progress

### ✅ Day 1 — Playwright Fundamentals
**File**: `Day1/test_playwright.py`

| Concept | API Used |
|---|---|
| Navigate to a URL | `page.goto()` |
| Assert the URL | `expect(page).to_have_url()` |
| Assert the page title | `expect(page).to_have_title()` |

---

### ✅ Practice: Browser Launch & Screenshots
**File**: `practice play-wright/practice- browser launch.py`

| Concept | API Used |
|---|---|
| Launch headed browser | `p.chromium.launch(headless=False)` |
| Slow down execution | `slow_mo=1000` |
| Take a screenshot | `page.screenshot(path="file.png")` |
| Get page title | `page.title()` |

---

### ✅ Practice: Locators — `get_by_role`
**File**: `practice play-wright/Locators/01_get_by_role.py`

| Concept | API Used |
|---|---|
| Find input by placeholder | `page.get_by_placeholder()` |
| Find button by role | `page.get_by_role("button", name="Login")` |
| Assert URL after action | `expect(page).to_have_url()` |
| Select first from multiple | `locator.first.click()` |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Playwright-SDET-QA.git
cd Playwright-SDET-QA
```

### 2. Set up a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 4. Run the Day 1 tests
```bash
python -m pytest Day1/
```

### 5. Run a standalone practice script
```bash
python "practice play-wright/practice- browser launch.py"
python "practice play-wright/Locators/01_get_by_role.py"
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.11+ | Core language |
| Playwright | 1.40+ | Browser automation |
| pytest | 7.4+ | Test runner |
| pytest-playwright | 0.4+ | Playwright-pytest integration |

---

## 📌 Key Locator Concepts

> "Always prefer **semantic locators** over CSS/XPath. They are resilient, readable, and accessible."

| Locator | When to Use |
|---|---|
| `get_by_role()` | ⭐ Best practice. Finds by button, link, heading, etc. |
| `get_by_placeholder()` | For form inputs with placeholder text |
| `get_by_label()` | For inputs linked to a `<label>` |
| `get_by_text()` | For any element by visible text |
| `get_by_test_id()` | When devs add `data-testid` attributes |

---

## 🧑‍💻 Author

Learning in public. Building toward SDET mastery one commit at a time.
