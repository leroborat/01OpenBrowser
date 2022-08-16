"""Template robot with Python."""

from RPA.Browser.Selenium import Selenium

browser = Selenium(auto_close=False)


def openBrowser():
    browser.open_available_browser()


def minimal_task():
    openBrowser()


if __name__ == "__main__":
    minimal_task()
