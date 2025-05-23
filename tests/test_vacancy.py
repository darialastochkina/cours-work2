from src.vacancy import Vacancy


def test_validation_and_attrs():
    """Проверка нормализации зарплаты и геттеров."""
    v1 = Vacancy("T", "C", 100, 200, "USD", "url")
    assert v1.title == "T"
    assert v1.company == "C"
    assert v1.salary_from == 100
    assert v1.salary_to == 200
    assert v1.currency == "USD"
    assert v1.url == "url"

    v2 = Vacancy("T2", "C2", None, None, None, "url2")
    assert v2.salary_from == 0
    assert v2.salary_to == 0
    assert v2.currency == "Не указано"


def test_str_and_to_dict():
    """Проверка to_dict() и __str__()."""
    v = Vacancy("Title", "Comp", 10, 20, "RUB", "u1")
    d = v.to_dict()
    assert d == {
        "title": "Title",
        "company": "Comp",
        "salary_from": 10,
        "salary_to": 20,
        "currency": "RUB",
        "url": "u1"
    }
    s = str(v)
    assert "Title | Comp | от 10" in s
    assert (
        "до 20" in s
        and "RUB" in s
        and "u1" in s
    )


def test_comparison():
    """Проверка операторов сравнения между Vacancy."""
    small = Vacancy("A", "C", 50, None, None, "u1")
    big = Vacancy("B", "C", 150, None, None, "u2")
    assert small < big
    assert big > small
    assert small == Vacancy("X", "Y", 50, None, None, "u3")
    assert not (small == big)
