import tkinter as tk
from tkinter import filedialog, ttk
import sys
import os
from tkinter import messagebox

# Подключение модулей
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from core.AutopartsProccessor import TableProcessor
from core.GeneralProccessor import ProcessorForOther
from core.AvitoProccessor import AvitoProc
import utils.const as const


class MyApp:
    def __init__(self, root):
        self.file_path = None  

        # Настройки главного окна
        root.title("Парсинг")
        root.geometry("800x500")
        root.configure(bg="#f4f4f4")

        main_frame = tk.Frame(root, bg="#f4f4f4", padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Блок выбора категории
        category_frame = tk.Frame(main_frame, bg="#ffffff", relief=tk.RIDGE, bd=2)
        category_frame.pack(fill=tk.X, pady=5)

        self.category = tk.StringVar(value="autoparts")
        tk.Label(category_frame, text="Выберите категорию:", font=("Arial", 10), bg="#ffffff").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(category_frame, text="Автозапчасти", variable=self.category, value="autoparts", bg="#ffffff", command=self.toggle_sheet_entry).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(category_frame, text="Общие товары", variable=self.category, value="general", bg="#ffffff", command=self.toggle_sheet_entry).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(category_frame, text="Авитовский прайс", variable=self.category, value="avito", bg="#ffffff", command=self.toggle_sheet_entry).pack(side=tk.LEFT, padx=5)

        # Блок выбора файла
        file_frame = tk.Frame(main_frame, bg="#ffffff", relief=tk.RIDGE, bd=2, padx=10, pady=10)
        file_frame.pack(fill=tk.X, pady=5)

        self.label_file = tk.Label(file_frame, text="Файл не выбран", font=("Arial", 10), bg="#ffffff")
        self.label_file.pack(side=tk.LEFT, padx=10)

        self.button_file = tk.Button(file_frame, text="Выбрать файл", command=self.choose_file, bg="#0078D7", fg="white")
        self.button_file.pack(side=tk.RIGHT, padx=10)

        # Блок ввода номера строки
        input_frame = tk.Frame(main_frame, bg="#ffffff", relief=tk.RIDGE, bd=2, padx=10, pady=10)
        input_frame.pack(fill=tk.X, pady=5)

        tk.Label(input_frame, text="Введите номер строки с шапкой:", font=("Arial", 10), bg="#ffffff").pack(side=tk.LEFT, padx=10)
        self.entry_number = tk.Entry(input_frame, width=10, bd=2)
        self.entry_number.pack(side=tk.LEFT, padx=10)

        # Поле ввода номера страницы (изначально скрыто)
        self.sheet_frame = tk.Frame(input_frame, bg="#ffffff")
        self.sheet_label = tk.Label(self.sheet_frame, text="Введите номер листа:", font=("Arial", 10), bg="#ffffff")
        self.entry_sheet = tk.Entry(self.sheet_frame, width=10, bd=2)

        self.button_process = tk.Button(input_frame, text="Запустить", command=self.run_method, bg="#28a745", fg="white")
        self.button_process.pack(side=tk.RIGHT, padx=10)

        # Блок логов
        log_frame = tk.Frame(main_frame, bg="#ffffff", relief=tk.RIDGE, bd=2, padx=10, pady=10)
        log_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.log_text = tk.Text(log_frame, height=10, width=90, state=tk.DISABLED, bg="#f8f8f8")
        self.log_text.pack(fill=tk.BOTH, expand=True, pady=5)

        scrollbar = tk.Scrollbar(log_frame, command=self.log_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=scrollbar.set)      
                  
        self.toggle_sheet_entry()  # Обновление UI при запуске

    def toggle_sheet_entry(self):
        """Показывает или скрывает поле ввода номера листа в зависимости от выбранной категории."""
        if self.category.get() == "avito":
            self.sheet_frame.pack(side=tk.LEFT, padx=10)
            self.sheet_label.pack(side=tk.LEFT)
            self.entry_sheet.pack(side=tk.LEFT, padx=5)
        else:
            self.sheet_frame.pack_forget()

    def choose_file(self):
        """Выбор файла"""
        self.file_path = filedialog.askopenfilename(filetypes=[("Все файлы", "*.*")])
        if self.file_path:
            self.label_file.config(text=f"Файл: {os.path.basename(self.file_path)}")
            self.log_message(f"Выбран файл: {self.file_path}")

    def run_method(self):
        """Запуск обработки данных"""
        try:
            number = int(self.entry_number.get())
        except ValueError:
            self.log_message("Ошибка: Введите корректный номер (целое число).")
            return

        sheet = None
        if self.category.get() == "avito":
            try:
                sheet = int(self.entry_sheet.get()) if self.entry_sheet.get() else 0
            except ValueError:
                self.log_message("Ошибка: Введите корректный номер листа (целое число).")
                return

        self.log_message(f"Запуск обработки: file_path={self.file_path}, number={number}, sheet={sheet}")

        if self.file_path:
            if self.category.get() == "autoparts":
                res = TableProcessor(self.file_path, number, const, 'output_auto.txt', self)
            elif self.category.get() == "general":
                res = ProcessorForOther(self.file_path, number, const, 'output_goods.txt', self)
            else:
                res = AvitoProc(self.file_path, number, sheet, const, "avito_price.txt", self)
            res.process_table()
            self.log_message(f"Файл обработан")
        else:
            self.log_message("Ошибка: Выберите файл и введите номер!")

    def log_message(self, message):
        """Добавляет сообщение в поле логов"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.config(state=tk.DISABLED)
        self.log_text.yview(tk.END)



# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
