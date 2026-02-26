"""
Day 1 - Playwright Fundamentals
================================
Concepts covered:
  - Basic navigation with page.goto()
  - URL assertion
  - Page title assertion
  - Using the `Page` fixture from pytest-playwright
"""

from playwright.sync_api import Page, expect


def test_verify_page_url(page: Page):
    """Verify that navigating to Automation Exercise returns the correct URL."""
    page.goto("https://automationexercise.com/")
    expect(page).to_have_url("https://automationexercise.com/")


def test_verify_page_title(page: Page):
    """Verify that the Automation Exercise homepage has the correct title."""
    page.goto("https://automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")