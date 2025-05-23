from typing import Optional


class Vacancy:
    """Класс для работы с вакансиями"""
    
    def __init__(
        self,
        title: str,
        url: str,
        salary_from: Optional[int],
        salary_to: Optional[int],
        description: str
    ):
        self.title = title
        self.url = self.__validate_url(url)
        self.salary_from = self.__validate_salary(salary_from)
        self.salary_to = self.__validate_salary(salary_to)
        self.description = description

    def __validate_url(self, url: str) -> str:
        """Валидация URL"""
        if not url.startswith("https://"):
            raise ValueError("Некорректный URL")
        return url

    def __validate_salary(self, salary: Optional[int]) -> int:
        """Валидация зарплаты"""
        return salary if salary is not None else 0

    def __lt__(self, other) -> bool:
        return self.salary_from < other.salary_from

    def __gt__(self, other) -> bool:
        return self.salary_from > other.salary_from

    def __eq__(self, other) -> bool:
        return self.salary_from == other.salary_from
