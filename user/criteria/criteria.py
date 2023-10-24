def get_citys() -> dict:
    all_citys = {
        'москва': 'moskva',
        'московская область': 'moskovskaya_oblast',
        'люберцы': 'lyubertsy',
        'коломна': 'kolomna',
        'мытищи': 'mytischi',

    }

    return all_citys


def get_count_rooms() -> dict:
    count_rooms = {
        'студия': 'studii',
        '1': '1-komnatnye',
        '2': '2-komnatnye',
        '3': '3-komnatnye',
        '4': '4-komnatnye',
        '5': '5-komnatnye'
    }

    return count_rooms


def get_types_rent() -> dict:
    type_rent = {
        'на длительный срок': 'na_dlitelnyy_srok',
        'посуточно': 'posutochno'
    }

    return type_rent


def get_filters() -> dict:
    output_filters = {
        'по умолчанию': '',
        'дороже': 's=2',
        'дешевле': 's=1',
        'по дате': 's=104'
    }
    return output_filters
