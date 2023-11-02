def get_page(data_criteria: dict) -> str:
    return f"https://www.avito.ru/{data_criteria['city']}/kvartiry/sdam/{data_criteria['type_rent']}/{data_criteria['count_rooms']}?{data_criteria['filter']}"


def get_next_page(url: str, number_page: int) -> str:
    return f"{url}?p={number_page}"
