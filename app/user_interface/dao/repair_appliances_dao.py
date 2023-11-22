import os
import sqlite3
from typing import List, Dict, Tuple


class RepairApplianceDAO:
    """Класс для работы с данными из БД - ремонт бытовой техники"""

    def __init__(self, path: str):
        """
        Инициализатор класса работы с данными - кино
        :param path: путь к БД
        """

        self.file_path = path

    def __repr__(self):
        """
        Представление для объектов класса
        :return: возвращает путь и его состояние
        """
        return f"Загрузчик Баз Данных по пути: {self.file_path} - {os.path.exists(self.file_path)}"

    def database_connect(self, query: str) -> List[Tuple[str, str, str, str, str]]:
        """
        Метод подключения к базе данных по запросу query
        :param query: запрос к БД
        :return: возвращает список кортежей с данными
        """
        with sqlite3.connect(self.file_path) as connect:
            cursor = connect.cursor()
            cursor.execute(query)
            return cursor.fetchall()



