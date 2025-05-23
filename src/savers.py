from abc import ABC, abstractmethod
import json
from typing import List
from .vacancy import Vacancy


class VacancySaver(ABC):
    """Абстрактный класс для сохранения/загрузки вакансий."""
    @abstractmethod
    def save_vacancies(self, vacancies: List[Vacancy]) -> None:
        pass

    @abstractmethod
    def load_vacancies(self) -> List[Vacancy]:
        pass

    @abstractmethod
    def delete_all(self) -> None:
        pass


class JSONSaver(VacancySaver):
    """Класс для работы с JSON-файлом"""
    
    def __init__(self, filename: str):
        self.__filename = filename

    def save_vacancies(self, vacancies: List[Vacancy]) -> None:
        """Сохраняет список вакансий в JSON-файл"""
        data = [vacancy.to_dict() for vacancy in vacancies]
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_vacancies(self) -> List[Vacancy]:
        """Загружает список вакансий из JSON-файла"""
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        return [
            Vacancy(
                title=item["title"],
                company=item["company"],
                salary_from=item.get("salary_from"),
                salary_to=item.get("salary_to"),
                currency=item.get("currency"),
                url=item["url"]
            )
            for item in data
        ]

    def delete_all(self) -> None:
        """Очищает файл, удаляя все вакансии."""
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump([], f)
