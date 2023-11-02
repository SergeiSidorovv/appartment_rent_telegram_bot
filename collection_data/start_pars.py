from aiogram.dispatcher import FSMContext
from selenium import webdriver

from collection_data import url_page
from collection_data import options_param
from collection_data import find_elements


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

                yield apartment_data

    except Exception as ex:
        print(ex)
    finally:
        if driver is not None:
            driver.quit()
