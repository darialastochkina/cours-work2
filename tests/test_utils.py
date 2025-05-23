from src.utils import filter_by_keyword, filter_by_min_salary, sort_by_salary
from src.vacancy import Vacancy


def mk(name, company, s_from, s_to, cur, url):
    """Хелпер для создания Vacancy."""
    return Vacancy(name, company, s_from, s_to, cur, url)


def test_filter_by_keyword():
    """Фильтрация по ключевому слову."""
    v1 = mk("Engineer", "TechCorp", 100, 150, "USD", "u1")
    v2 = mk("Manager", "BizCorp", 200, 250, "USD", "u2")
    res = filter_by_keyword([v1, v2], "engine")
    assert v1 in res and v2 not in res


def test_filter_by_min_salary():
    """Фильтрация по минимальной зарплате."""
    v1 = mk("Dev", "A", 50, None, None, "u1")
    v2 = mk("Dev2", "B", 150, None, None, "u2")
    res = filter_by_min_salary([v1, v2], 100)
    assert v2 in res and v1 not in res


def test_sort_by_salary():
    """Сортировка вакансий по зарплате (убывание)."""
    v1 = mk("Low", "A", 50, None, None, "u1")
    v2 = mk("High", "B", 150, None, None, "u2")
    res = sort_by_salary([v1, v2])
    assert res == [v2, v1]
