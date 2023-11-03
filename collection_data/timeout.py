from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


def wait_download_start_page(driver: webdriver):

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "styles-module-theme-CRreZ")))
