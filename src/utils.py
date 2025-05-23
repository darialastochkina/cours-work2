from typing import List
from src.vacancy import Vacancy


def filter_by_keyword(vacancies: List[Vacancy], keyword: str) -> List[Vacancy]:
    """Оставляет вакансии, где keyword встречается в названии или компании."""
    k = keyword.lower()
    return [v for v in vacancies if k in v.title.lower() or k in v.company.lower()]


def filter_by_min_salary(vacancies: List[Vacancy], min_salary: int) -> List[Vacancy]:
    """Оставляет вакансии с минимальной зарплатой ≥ min_salary."""
    return [v for v in vacancies if v.salary_from >= min_salary]


def sort_by_salary(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортирует вакансии по минимальной зарплате по убыванию."""
    return sorted(vacancies, key=lambda v: v.salary_from, reverse=True)
