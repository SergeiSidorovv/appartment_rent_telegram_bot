from aiogram.dispatcher import FSMContext
from selenium import webdriver
import time

from collection_data import url_page, options_param, find_elements, timeout


async def collection_data(data_criteria: FSMContext) -> dict:
    try:
        url = url_page.get_page(data_criteria)
        driver = None
        process = True
        number_page = 1
        apartment_data = {}

        while process:
            driver = webdriver.Chrome(options=options_param.get_options())
            driver.get(url)
            timeout.wait_download_start_page(driver)
            list_appartments = find_elements.get_all_appartments_on_page(
                driver)
            if len(list_appartments) == 0:
                process = False
                driver.close()
                yield apartment_data

            else:
                url_appartments = find_elements.get_url_appartments(
                    list_appartments)
                info_appartments = find_elements.get_info_appartments(driver)
                price_appartments = find_elements.get_price(driver)

                apartment_data['url'] = url_appartments
                apartment_data['info'] = info_appartments
                apartment_data['price'] = price_appartments

                number_page += 1

                driver.close()

                url = url_page.get_next_page(url, number_page)

                yield apartment_data

    except Exception as ex:
        print(ex)
    finally:
        if driver is not None:
            driver.quit()
