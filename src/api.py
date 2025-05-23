import requests
from typing import List
from .vacancy import Vacancy


class HeadHunterAPI:
    """Класс для работы с API HeadHunter"""
    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword: str, per_page: int = 20) -> List[Vacancy]:
        """Получает список вакансий по ключевому слову"""
        params = {"text": keyword}
        if per_page is not None:
            params["per_page"] = per_page

        try:
            resp = requests.get(self.BASE_URL, params=params)
            resp.raise_for_status()
        except requests.RequestException:
            return []

        items = resp.json().get("items", [])
        return [self._parse(item) for item in items]

    @staticmethod
    def _parse(item: dict) -> Vacancy:
        """Преобразует dict в объект Vacancy"""
        salary = item.get("salary") or {}
        return Vacancy(
            title=item.get("name", ""),
            company=item.get("employer", {}).get("name", ""),
            salary_from=salary.get("from"),
            salary_to=salary.get("to"),
            currency=salary.get("currency"),
            url=item.get("alternate_url", "")
        )
