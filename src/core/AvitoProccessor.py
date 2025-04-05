import pandas as pd
import utils.const as const
from transliterate.decorators import transliterate_function

class AvitoProc:
    def __init__(self, file_path: str, header_row: int, sheet ,synonyms: dict, output_file: str, app):

        self.file_path = file_path
        self.header_row = header_row   
        self.synonyms = const.CARVERS_FOR_AVITO 
        self.output_file = output_file
        self.app = app
        self.sheet = sheet
        self.data = self._load_file()
        
    
    def _load_file(self):
        """Определяет формат файла и загружает его."""
        try:
            if self.file_path.endswith(".csv"):
                return pd.read_csv(self.file_path, header=self.header_row)
            elif self.file_path.endswith(".xls") or self.file_path.endswith(".xlsx"):
                return pd.read_excel(self.file_path, header=self.header_row, sheet_name=self.sheet)
            else:
                self.app.log_message(f"Неверный формат файла")      
        except Exception as e:        
            self.app.log_message(f"Ошибка при загрузке таблицы: {e}") 
    
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
            return f'\t\t\t\t\t\t\t\t<entry><bean class="dataNullCarver"/></entry>'
        
        except Exception as e:
            self.app.log_message(f'Произошла ошибка: {e}')

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


