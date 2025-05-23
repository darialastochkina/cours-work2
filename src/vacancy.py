from typing import Optional


class Vacancy:
    """
    Класс-вакансия с инкапсуляцией и методами сравнения.
    """
    __slots__ = (
        "__title", "__company", "__salary_from",
        "__salary_to", "__currency", "__url"
    )

    def __init__(
        self,
        title: str,
        company: str,
        salary_from: Optional[int],
        salary_to: Optional[int],
        currency: Optional[str],
        url: str
    ) -> None:
        """Создает вакансию и валидирует зарплату."""
        self.__title = title
        self.__company = company
        self.__salary_from = self.__validate_salary(salary_from)
        self.__salary_to = self.__validate_salary(salary_to)
        self.__currency = currency or "Не указано"
        self.__url = url

    @staticmethod
    def __validate_salary(val: Optional[int]) -> int:
        """Возвращает положительную зарплату или 0."""
        return val if isinstance(val, int) and val > 0 else 0

    @property
    def title(self) -> str:
        return self.__title

    @property
    def company(self) -> str:
        return self.__company

    @property
    def salary_from(self) -> int:
        return self.__salary_from

    @property
    def salary_to(self) -> int:
        return self.__salary_to

    @property
    def currency(self) -> str:
        return self.__currency

    @property
    def url(self) -> str:
        return self.__url

    def to_dict(self) -> dict:
        """Преобразует вакансию в словарь."""
        return {
            "title": self.__title,
            "company": self.__company,
            "salary_from": self.__salary_from,
            "salary_to": self.__salary_to,
            "currency": self.__currency,
            "url": self.__url
        }

    def __str__(self) -> str:
        """Строковое представление вакансии."""
        base = f"{self.__title} | {self.__company} | от {self.__salary_from}"
        if self.__salary_to:
            base += f" до {self.__salary_to}"
        return f"{base} {self.__currency} | {self.__url}"

    def __lt__(self, other: object) -> bool:
        """Сравнение по минимальной зарплате (меньше)."""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.__salary_from < other.__salary_from

    def __gt__(self, other: object) -> bool:
        """Сравнение по минимальной зарплате (больше)."""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.__salary_from > other.__salary_from

    def __eq__(self, other: object) -> bool:
        """Равенство по минимальной зарплате."""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.__salary_from == other.__salary_from
