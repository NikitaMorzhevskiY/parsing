import re
import csv 

import pandas as pd

import utils.templates as templates
import utils.func as func 
from  utils.carvers import ALL_CARVERS 


class GeneralHandler:
    def __init__(self, file_path: str, header_row: int, synonyms: dict, output_file: str, app):

        self.file_path = file_path
        self.header_row = header_row
        self.synonyms = templates.CARVERS_FOR_UKV
        self.output_file = output_file
        self.app = app
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
                return pd.read_csv(self.file_path, sep=delimiter, header=self.header_row, encoding='utf-8')

            elif self.file_path.endswith(".xls") or self.file_path.endswith(".xlsx"):
                return pd.read_excel(self.file_path, header=self.header_row)

            else:
                self.app.log_message("Неверный формат файла")

        except Exception as e:
            self.app.log_message(f"Ошибка при загрузке таблицы: {e}")
            return None


    def process_table(self):
        """Проходит по наименованиям колонки, исходя из них вставляет в 
            словарь подходящий фрагмент xml как значение и ключ, который так же указан 
            в templates. Если находит колонку наименование, то в func идет вставка подходящик 
            карверов, вставляются и в описание и в наименование исходя из carvers. В результат описание
            с карверами попадает только после нахождения этой колонки, временно хранится в pending_fata
        """
        result = {}
        pending_data = {"Наименование": [], "Описание": []}  
        try:
            self.app.log_message("Обработка файла запущена...")
            for column_index, column in enumerate(self.data.columns):
                xml_fragment = self._map_values(column)

                if isinstance(xml_fragment, tuple):

                    key, value = xml_fragment
                    
                    if key in result:
                        if key in ['Наименование', 'Описание']: 
                            result[key].extend(value)
                        else :                  #для повторных колонок
                            key_column = f"{key}_{column}"
                            result[key_column] = [value]
                    else:
                        result[key] = [value]
                    
                    if key == 'Наименование':

                        additional_data = func.split_carver_name_descr(self.return_items_cilumn(column), ALL_CARVERS)
                        
                        
                        for add_key, add_values in additional_data.items():
                            pending_data[add_key].extend(add_values) 

                else:

                    value = xml_fragment
                    unique_key = f"{column_index}"

                    if unique_key in result:
                        result[unique_key].append(value)
                    else:
                        result[unique_key] = [value]

                
                if re.search(r"\b(наименовани[ея]\s*(товар[а|ов])?|Номенклатура\,\sУпаковка|название)\b", column, re.IGNORECASE) and pending_data["Наименование"]:            #Заменил column на key - потестить то ли это, кажется хуйня какая то
                    if "Наименование" in result:
                        result["Наименование"].extend(pending_data["Наименование"])
                    else:
                        result["Наименование"] = pending_data["Наименование"]

                    if "Описание" in result and "Описание" in pending_data:
                        result["Описание"].extend(pending_data["Описание"])  

                    pending_data["Наименование"] = []  

            
                if re.search(r"\bописание\b", column, re.IGNORECASE) and pending_data["Описание"]:
                    if "Описание" in result:
                        result["Описание"].extend(pending_data["Описание"])
                    else:
                        result["Описание"] = pending_data["Описание"]

                    if "Наименование" in result and "Наименование" in pending_data:
                        result["Наименование"].extend(pending_data["Наименование"])  
                            
                    pending_data["Описание"] = [] 

                   

            self._save_result(result)
 
        except Exception as e:

            self.app.log_message(f"Ошибка при обработке: {e}")     

    
    def _map_values(self, column_name:str) -> str:
        """Находит совпадения для заданного названия колонки в файле templates"""
        try:
            for key, value in self.synonyms.items():
            
                if value["synonyms"].search(column_name):  

                    return key, value["xml"]
                
           
            
            return f'<entry><bean class="dataNullCarver"/></entry>'
        
        except  Exception as e:
                self.app.log_message(f"Ошибка при обработке в поиске ключа(map_values): {e}")
    

    def _save_result(self, result: list):
        """Сохраняет результат в файл"""
        try:
            with open(self.output_file, "w", encoding="utf-8") as f:

                for key, value in result.items():

                    if key in ["Описание", "Наименование"]:

                        f.write(f'<entry>\n\t<bean class="dataCompositeCarver">\n'
                            f'\t\t<constructor-arg>\n\t\t\t<list>\n{"\n".join(value)}\n\t\t\t</list>\n'
                            f'\t\t</constructor-arg>\n\t</bean>\n</entry>')   
                        f.write("\n") 
                        
                    else:    
                        f.write("\n".join(value))
                        f.write("\n")
        except Exception as e:
            self.app.log_message(f'Ошибка при сохранении: {e}')            
                
    

    def return_items_cilumn(self, column_name):
        
        return self.data[column_name].tolist()

        