import pytest
from src.savers import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def tmp_file(tmp_path):
    """Временное имя JSON-файла для тестов."""
    return str(tmp_path / "test.json")


def test_save_and_load_and_delete(tmp_file):
    """Проверка save/load/delete в JSONSaver."""
    saver = JSONSaver(tmp_file)
    assert saver.load_vacancies() == []

    vac1 = Vacancy("T1", "C1", 100, 200, "USD", "u1")
    vac2 = Vacancy("T2", "C2", None, None, None, "u2")
    saver.save_vacancies([vac1, vac2])

    loaded = saver.load_vacancies()
    assert len(loaded) == 2
    assert any(v.title == "T1" and v.url == "u1" for v in loaded)
    assert any(v.title == "T2" and v.url == "u2" for v in loaded)

    saver.save_vacancies([vac1])
    loaded2 = saver.load_vacancies()
    assert len(loaded2) == 2

    saver.delete_all()
    assert saver.load_vacancies() == []
