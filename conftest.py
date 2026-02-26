"""
conftest.py — Root-Level Shared Fixtures
==========================================
Automatically loaded by pytest before any test.
Fixtures defined here are available to ALL tests in the project.

Fixture Scopes:
  - function  : Created fresh for every single test (default)
  - module    : Shared across all tests in one file
  - session   : Shared across the entire test run (fastest, use carefully)
"""

import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="session")
def base_url() -> str:
    """Central base URL - change once, applies everywhere."""
    return "https://automationexercise.com"


@pytest.fixture(scope="session")
def saucedemo_credentials() -> dict:
    """Shared login credentials for SauceDemo tests."""
    return {
        "username": "standard_user",
        "password": "secret_sauce",
    }


# ── Future fixtures to add as you progress ────────────────────────────────────
# @pytest.fixture
# def logged_in_page(page: Page, saucedemo_credentials):
#     """Returns a page already logged in to SauceDemo."""
#     page.goto("https://www.saucedemo.com")
#     page.get_by_placeholder("Username").fill(saucedemo_credentials["username"])
#     page.get_by_placeholder("Password").fill(saucedemo_credentials["password"])
#     page.get_by_role("button", name="Login").click()
#     return page
