import pandas as pd
import utils.const as const
from transliterate.decorators import transliterate_function


class TableProcessor:
    def __init__(self, file_path: str, header_row: int, synonyms: dict, output_file: str, app):

        self.file_path = file_path
        self.header_row = header_row   
        self.synonyms = const.CARVERS_FOR_AUTO    
        self.output_file = output_file
        self.app = app
        self.data = self._load_file()
        
    
    def _load_file(self):
        """Определяет формат файла и загружает его."""

        if self.file_path.endswith(".csv"):
            return pd.read_csv(self.file_path, header=self.header_row)
        elif self.file_path.endswith(".xls") or self.file_path.endswith(".xlsx"):
            return pd.read_excel(self.file_path, header=self.header_row)
        else:
            self.app.log_message(f"Неверный формат файла")      
    
    def process_table(self):
        """Обрабатывает таблицу и формирует текстовый результат."""
        result = []

        try:

            for column in self.data.columns:
                xml_fragment = self._map_values_autoparts(column)
                if xml_fragment:
                    result.append(xml_fragment)
            self._save_result(result)

        except Exception as e:

            self.app.log_message(f"Ошибка при обработке: {e}") 
    
    def _map_values_autoparts(self, column_name:str) -> str:
        """Находит ключ по регулярному выражению и возвращает соответствующий XML."""
        try:

            for key, value in self.synonyms.items():
                if value["synonyms"].search(column_name):  
                    return value["xml"]
            return f'<entry><bean class="dataNullCarver"/></entry>'
        
        except Exception as e:
            self.app.log_message(f'Произошла ошибка: {e}')
    
    # def _map_values_other(self, column_name:str):  Починить как то надо 
    #     for key, value in self.synonyms.items():
    #         if value["synonyms"].search(column_name):  
    #             if key.lower() in ['описание', 'наименование']:
    #                 temp = func.split_carver_name_descr(self.return_items_cilumn(key)) 
    #                 if key.lower() == 'описание':
    #                     name = temp['Наименование']
    #                     return f'<entry>\n<bean class="dataCompositeCarver">\n<constructor-arg>\n<list>{temp}</list>\n</constructor-arg>\n</bean>\n</entry>'
    #             else:
    #               pass   #тут нужно проверять значения колонки / вставить функцию проверки значений. Функция должна находить слова и возвращать пак карверов по этим словам
                        
                    
    #             return value["xml"]
    #     return f'<entry><bean class="dataNullCarver"/></entry>'

    def _save_result(self, result: list):
        """Сохраняет обработанный текст в файл."""
        try:

            with open(self.output_file, "w", encoding="utf-8") as f:
                f.write("\n".join(result))
                
        except Exception as e:
            self.app.log_message(f'Ошибка при сохранении: {e}')     

    @transliterate_function(language_code='ru', reversed=True)
    def translit(self, text: str) -> str:   
        """Переводит кирилицу в латиницу"""   

        return text
    
    def return_items_cilumn(self, column_name):
 
        return self.data[column_name].tolist()


