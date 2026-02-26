"""
conftest.py — Shared Pytest Fixtures
======================================
This file is automatically loaded by pytest before any test runs.
Add shared fixtures here as the project grows.

Common future fixtures:
  - browser context with custom viewport
  - authenticated page (pre-logged-in state)
  - base URL configuration
"""

import pytest
from playwright.sync_api import Page


# Example fixture: can be extended in future days
@pytest.fixture(scope="session")
def base_url():
    """Return the base URL for tests that need it."""
    return "https://automationexercise.com"
