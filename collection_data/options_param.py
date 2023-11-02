from selenium import webdriver


def get_options():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    return options
