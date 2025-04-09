import utils.carvers as carvers   
import re
from collections import defaultdict


def split_carver_name_descr(column: list, carvers_dict: dict) -> dict:
    """
    Принимает список значений из колонки таблицы и словарь с карверами.
    Возвращает словарь с секциями 'Наименование' и 'Описание' и соответствующими XML.
    """
    result = defaultdict(list)

    for item in column:
        item_lower = str(item).lower()
        words = re.findall(r'\b[\w-]+\b', item_lower)

        for keywords, carver_sections in carvers_dict.items():
            for word in words:
                if word in keywords:
                    for section, xml in carver_sections.items():
                        entry = f"{xml} {word}"
                        if entry not in result[section]:
                            result[section].append(entry)
                    break  # больше не ищем в этом carvers_dict
            else:
                continue
            break

    return dict(result)