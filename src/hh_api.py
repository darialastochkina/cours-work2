from abc import ABC, abstractmethod
import requests
from typing import List, Dict, Any


class APIHandler(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""
    
    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Получает вакансии по ключевому слову"""
        pass


class HeadHunterAPI(APIHandler):
    """Класс для работы с API HeadHunter"""
    
    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__params = {
            "area": 113,  # Россия
            "per_page": 100
        }
        
    def get_vacancies(self, keyword: str) -> List[Dict]:
        """
        Получает вакансии с HH.ru по ключевому слову
        
        Args:
            keyword: Поисковый запрос
        Returns:
            Список вакансий
        """
        self.__params["text"] = keyword
        response = requests.get(self.__base_url, params=self.__params)
        if response.status_code != 200:
            raise ConnectionError("Ошибка получения вакансий")
        return response.json()["items"] 