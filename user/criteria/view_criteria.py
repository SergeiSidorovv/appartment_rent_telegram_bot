

async def view_citys(dict_citys: dict) -> str:
    str_all_citys = "Доступные города"
    str_all_citys += "\n"
    for city in dict_citys.keys():
        str_all_citys += city.title()
        str_all_citys += "\n"

    return str_all_citys


async def view_count_rooms(dict_count_rooms: dict) -> str:
    str_count_rooms = "Доступное количество комнат:'"
    str_count_rooms += '\n'
    for count_rooms in dict_count_rooms.keys():
        str_count_rooms += count_rooms.title()
        str_count_rooms += '\n'

    return str_count_rooms


async def view_filters(dict_filters_output: dict) -> str:
    str_filters = 'Доступные фильтры:'
    str_filters += '\n'
    for filter in dict_filters_output.keys():
        str_filters += filter.title()
        str_filters += '\n'

    return str_filters
