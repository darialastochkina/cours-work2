from abc import ABC, abstractmethod
import requests
from typing import List
from src.vacancy import Vacancy


class JobAPI(ABC):
    """Абстрактный класс для работы с API вакансий."""
    @abstractmethod
    def connect(self) -> bool:
        """Проверить доступность API."""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, per_page: int = 20) -> List[Vacancy]:
        """Получить список вакансий по ключевому слову."""
        pass


class HeadHunterAPI(JobAPI):
    """Клиент для hh.ru."""
    _BASE_URL = "https://api.hh.ru/vacancies"

    def connect(self) -> bool:
        try:
            resp = requests.get(self._BASE_URL)
            resp.raise_for_status()
            return True
        except requests.RequestException:
            return False

    def get_vacancies(self, keyword: str, per_page: int = 20) -> List[Vacancy]:
        if not self.connect():
            return []
        params = {"text": keyword, "per_page": per_page, "page": 0}
        resp = requests.get(self._BASE_URL, params=params)
        resp.raise_for_status()
        items = resp.json().get("items", [])
        return [self._parse(item) for item in items]

    @staticmethod
    def _parse(item: dict) -> Vacancy:
        sal = item.get("salary") or {}
        return Vacancy(
            title=item.get("name", "Не указано"),
            company=item.get("employer", {}).get("name", "Не указано"),
            salary_from=sal.get("from"),
            salary_to=sal.get("to"),
            currency=sal.get("currency"),
            url=item.get("alternate_url", "")
        )
