from abc import ABC, abstractmethod
import json
from typing import List
from src.vacancy import Vacancy


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
    """Реализация VacancySaver для JSON-файла."""
    def __init__(self, filename: str = "vacancies.json") -> None:
        """Инициализирует сохранитель с именем JSON-файла."""
        self.__filename = filename

    def save_vacancies(self, vacancies: List[Vacancy]) -> None:
        """Сохраняет вакансии в файл, обновляя по URL без дубликатов."""
        existing = self.load_vacancies()
        store = {v.url: v.to_dict() for v in existing}
        for v in vacancies:
            store[v.url] = v.to_dict()
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(list(store.values()), f, ensure_ascii=False, indent=4)

    def load_vacancies(self) -> List[Vacancy]:
        """Загружает вакансии из JSON-файла, возвращает список Vacancy."""
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
