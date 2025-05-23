from src.api import HeadHunterAPI
from src.savers import JSONSaver
from src.utils import filter_by_keyword, filter_by_min_salary, sort_by_salary


def main() -> None:
    """Собирает, фильтрует и выводит вакансии по заданным критериям."""
    api = HeadHunterAPI()
    saver = JSONSaver()

    query = input("🔎 Введите поисковый запрос: ")
    per_page = int(input("📄 Сколько вакансий загрузить: "))
    min_salary = int(input("💰 Минимальная зарплата: "))
    top_n = int(input("🏆 Сколько топ-вакансий показать: "))

    vacancies = api.get_vacancies(query, per_page=per_page)
    saver.save_vacancies(vacancies)

    filtered_kw = filter_by_keyword(vacancies, query)
    filtered = filter_by_min_salary(filtered_kw, min_salary)
    sorted_all = sort_by_salary(filtered)

    for vac in sorted_all[:top_n]:
        print(vac)


if __name__ == "__main__":
    main()
