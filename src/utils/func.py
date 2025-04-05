import utils.carvers as carvers

def split_carver_name_descr(column: list) -> dict:
    """
    Принимает список значений из колонки таблицы и возвращает словарь с карверами 
    для наименования и описания, проходя по всем словарям в файле const.
    """
    result = {
        'Наименование': [],
        'Описание': []
    }
    
    # Проходим по всем атрибутам модуля const
    for attr_name in dir(carvers):
        if attr_name.isupper():  #нужные словари именуются заглавными буквами
            furniture_templates = getattr(carvers, attr_name)
            if isinstance(furniture_templates, dict):  # Проверяем словарь ли это
                for item in column:
                    item_lower = str(item).lower()
                    
                    for keys, data in furniture_templates.items():
                        if any(word in item_lower for word in (keys if isinstance(keys, (list, tuple)) else [keys])):
                            for section, template in data.items():
                                if template not in result[section]:
                                    result[section].append(template)
    
    return result