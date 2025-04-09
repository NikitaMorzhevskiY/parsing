import csv

import pandas as pd

import utils.templates as templates


class AvitoHandler:
    def __init__(self, file_path: str, header_row: int, sheet ,synonyms: dict, output_file: str, app):

        self.file_path = file_path
        self.header_row = header_row   
        self.template = templates.CARVERS_FOR_AVITO 
        self.output_file = output_file
        self.app = app
        self.sheet = sheet
        self.data = self._load_file()
        
    
    def _load_file(self):
        try:
            if self.file_path.endswith(".csv"):
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    sample = f.read(2048)
                    f.seek(0)

                    try:
                        dialect = csv.Sniffer().sniff(sample)
                        delimiter = dialect.delimiter
                    except csv.Error:
                        delimiter = ','

                    self.app.log_message(f"Определён разделитель: '{delimiter}'")

                # читаем CSV с определённым разделителем
                return pd.read_csv(self.file_path, sep=delimiter, header=self.header_row, encoding='utf-8', nrows=100)

            elif self.file_path.endswith(".xls") or self.file_path.endswith(".xlsx"):
                return pd.read_excel(self.file_path, header=self.header_row, sheet_name=self.sheet, nrows=100)

            else:
                self.app.log_message("Неверный формат файла")

        except Exception as e:
            self.app.log_message(f"Ошибка при загрузке таблицы: {e}")
            return None
    
    def process_table(self):
        """Идет по названиям колонок из шапки и формирует массив из подходящих фрагментов"""
        result = []

        try:

            for column in self.data.columns:
                xml_fragment = self._map_values(column)
                if xml_fragment:
                    result.append(xml_fragment)
            self._save_result(result)

        except Exception as e:

            self.app.log_message(f"Ошибка при обработке: {e}") 
    
    def _map_values(self, column_name:str) -> str:
        """Находит совпадения для заданного названия колонки в файле templates"""
        try:

            for key, value in self.template.items():
                if value["synonyms"].search(column_name):  
                    return value["xml"]
            return f'\t\t\t\t<entry><bean class="dataNullCarver"/></entry>'
        
        except Exception as e:
            self.app.log_message(f'Произошла ошибка: {e}')

    def _save_result(self, result: list):
        """Сохраняет результат в файл"""
        try:

            with open(self.output_file, "w", encoding="utf-8") as f:
                f.write("\n".join(result))
                
        except Exception as e:
            self.app.log_message(f'Ошибка при сохранении: {e}')     

   


