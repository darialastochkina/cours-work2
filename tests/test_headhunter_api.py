import requests
from src.api import HeadHunterAPI
from src.vacancy import Vacancy


class DummyResponse:
    """Mocked HTTP response for requests.get."""
    def __init__(self, status_code=200, json_data=None):
        self.status_code = status_code
        self._json = json_data or {"items": []}

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(f"HTTP {self.status_code}")

    def json(self):
        return self._json


def dummy_get(url, params=None):
    """Возвращает DummyResponse для проверки connect()/get_vacancies."""
    if params is None:
        return DummyResponse(status_code=200)
    item = {
        "name": "TestVac",
        "employer": {"name": "TestCo"},
        "salary": {"from": 100, "to": 200, "currency": "USD"},
        "alternate_url": "http://test"
    }
    return DummyResponse(status_code=200, json_data={"items": [item]})


def test_get_vacancies_success(monkeypatch):
    """Успешный вызов get_vacancies возвращает список Vacancy."""
    monkeypatch.setattr("requests.get", dummy_get)
    api = HeadHunterAPI()
    result = api.get_vacancies("python", per_page=1)
    assert isinstance(result, list)
    assert len(result) == 1
    vac = result[0]
    assert isinstance(vac, Vacancy)
    assert vac.title == "TestVac"
    assert vac.company == "TestCo"
    assert vac.salary_from == 100
    assert vac.salary_to == 200
    assert vac.currency == "USD"
    assert vac.url == "http://test"


def test_get_vacancies_connect_fail(monkeypatch):
    """При ошибке соединения get_vacancies возвращает пустой список."""
    def fail_get(url, params=None):
        raise requests.RequestException("fail")
    monkeypatch.setattr("requests.get", fail_get)
    api = HeadHunterAPI()
    assert api.get_vacancies("x") == []
