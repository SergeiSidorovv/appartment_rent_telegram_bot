from selenium import webdriver
from selenium.webdriver.common.by import By


def get_all_appartments_on_page(driver: webdriver) -> list:

    webelements_appatrments = driver.find_element(
        By.CLASS_NAME, 'items-items-kAJAg').find_elements(
        By.CLASS_NAME, 'iva-item-sliderLink-uLz1v')

    return webelements_appatrments


def get_info_appartments(driver: webdriver) -> list:
    webelement_appartments = driver.find_element(
        By.CLASS_NAME, 'items-items-kAJAg').find_elements(
        By.CLASS_NAME, 'iva-item-title-py3i_')

    info_appartment = [i.get_attribute(
        'textContent').replace("\xa0", " ") for i in webelement_appartments]
    return info_appartment


def get_url_appartments(list_appartments: list) -> list:
    url_appartments = []
    for i in list_appartments:
        url_appartments.append(i.get_attribute(
            'href') + '?guests=2')
    return url_appartments


def get_price(driver: webdriver) -> list:
    webelement_prices = driver.find_element(
        By.CLASS_NAME, 'items-items-kAJAg').find_elements(
        By.CLASS_NAME, 'styles-module-root-LIAav')

    price_appartments = [i.get_attribute(
        'textContent').replace("\xa0", " ") for i in webelement_prices]
    return price_appartments
