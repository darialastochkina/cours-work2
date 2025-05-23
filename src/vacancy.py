from typing import Optional


class Vacancy:
    """Класс для работы с вакансиями"""
    def __init__(
        self,
        title:       str,
        company:     str,
        salary_from: Optional[int],
        salary_to:   Optional[int],
        currency:    Optional[str],
        url:         str
    ) -> None:
        """Описывает вакансию и валидирует входные данные."""
        self.title = title
        self.company = company

        self.salary_from = (
            salary_from if isinstance(salary_from, int) and salary_from > 0 else 0
        )
        self.salary_to = (
            salary_to if isinstance(salary_to, int) and salary_to > 0 else 0
        )

        if not (url.startswith("http://") or url.startswith("https://")):
            raise ValueError(f"Некорректный URL: {url}")
        self.url = url

        self.currency = currency

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
