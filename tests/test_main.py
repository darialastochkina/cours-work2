import builtins
import pytest
import main
from src.vacancy import Vacancy
from src.api import HeadHunterAPI


@pytest.fixture(autouse=True)
def patch_saver(monkeypatch):
    """Меняет JSONSaver на пустой класс, чтобы не писать в файл."""
    class DummySaver:
        def __init__(self, *args, **kwargs): pass
        def save_vacancies(self, vacs): pass
    monkeypatch.setattr(main, "JSONSaver", DummySaver)


def test_main_no_vacancies(monkeypatch, capsys):
    """Если API вернул пусто, main ничего не печатает."""
    inputs = iter(["", "5", "0", "3"])
    monkeypatch.setattr(
        builtins,
        "input",
        lambda prompt="": next(inputs),
    )
    monkeypatch.setattr(
        HeadHunterAPI,
        "get_vacancies",
        lambda self, q, per_page=None: [],
    )
    main.main()
    assert capsys.readouterr().out == ""


def test_main_with_vacancies(monkeypatch, capsys):
    """main выводит топ-N вакансий после фильтрации по min_salary."""
    vac1 = Vacancy("Low", "C", 100, None, "USD", "u1")
    vac2 = Vacancy("High", "C", 200, None, "USD", "u2")
    inputs = iter(["", "2", "150", "2"])
    monkeypatch.setattr(
        builtins,
        "input",
        lambda prompt="": next(inputs),
    )
    monkeypatch.setattr(
        HeadHunterAPI,
        "get_vacancies",
        lambda self, q, per_page=None: [vac1, vac2],
    )
    main.main()
    out = capsys.readouterr().out.strip().splitlines()
    assert out == [str(vac2)]
