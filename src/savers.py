from abc import ABC, abstractmethod
import json
from typing import List
from .vacancy import Vacancy


class VacancySaver(ABC):
    """Abstract base class for saving vacancies"""
    @abstractmethod
    def save_vacancies(self, vacancies: List[Vacancy]) -> None:
        """Save vacancies to storage"""
        pass

    @abstractmethod
    def load_vacancies(self) -> List[Vacancy]:
        pass

    @abstractmethod
    def delete_all(self) -> None:
        pass


class JSONSaver(VacancySaver):
    """Class for working with JSON files"""
    def __init__(self, filename: str = "vacancies.json"):
        """
        Initialize JSONSaver
        """
        self.__filename = filename

    def save_vacancies(self, vacancies: List[Vacancy]) -> None:
        """
        Save vacancies to JSON file, avoiding duplicates
        """
        existing_vacancies = []
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                existing_vacancies = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        existing_urls = {vacancy["url"] for vacancy in existing_vacancies}
        new_vacancies = [
            vacancy.to_dict() for vacancy in vacancies
            if vacancy.url not in existing_urls
        ]
        all_vacancies = existing_vacancies + new_vacancies
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(all_vacancies, f, ensure_ascii=False, indent=2)

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
