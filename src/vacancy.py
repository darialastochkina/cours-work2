from typing import Optional, Dict


class Vacancy:
    """Класс для работы с вакансиями"""
    def __init__(self, title: str, salary: Optional[Dict], url: str, description: str):
        """
        Initialize Vacancy instance
        """
        self.__validate_title(title)
        self.__validate_url(url)
        self.__validate_description(description)
        self.title = title
        self.url = url
        self.description = description
        self.salary = self.__process_salary(salary)

    def __validate_url(self, url: str) -> str:
        """Валидация URL"""
        if not url.startswith("http"):
            raise ValueError("Некорректный URL")
        return url

    def __validate_salary(self, salary: Optional[int]) -> int:
        """Валидация зарплаты"""
        return salary if salary is not None else 0

    def __lt__(self, other): return self.salary_from < other.salary_from
    def __gt__(self, other): return self.salary_from > other.salary_from
    def __eq__(self, other): return self.salary_from == other.salary_from

    def to_dict(self) -> dict:
        """Преобразование в словарь для сохранения в JSON"""
        return {
            "title": self.title,
            "company": self.company,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "currency": self.currency,
            "url": self.url
        }
