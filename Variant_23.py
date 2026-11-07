"""Хранение данных о городах на основе списков и словарей."""
import csv

FIELDS = ["name", "year", "population", "country"]
FILE = "cities.csv"

def load_records(filename=FILE):
    """Загрузка записей о городах из файла, возвращает список словарей."""
    cities = []
    try:
        with open(filename, 'r', encoding="utf-8", newline='') as city_records:
            reader = csv.DictReader(city_records)
            for row in reader:
                cities.append({
                    "name": row["name"],
                    "year": int(row["year"]),
                    "population": int(row["population"]),
                    "country": row["country"],
                })
    except FileNotFoundError:
        pass
    return cities

def save_records(cities, filename=FILE):
    """Сохранить список словарей с данными о городах в файл csv."""
    with open(filename, 'w', encoding="utf-8", newline='') as city_records:
        writer = csv.DictWriter(city_records, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(cities)

def add_record(cities):
    """Добавление словаря с данными о городе в список."""
    name = input("Наименование: ").strip()
    try:
        year = int(input("Год основания: "))
        population = int(input("Население: "))
    except ValueError:
        print("Введено некорректное значение.")
        return
    country = input('Страна: ').strip()
    city = {"name": name,
              "year": year,
              "population": population,
              "country": country}
    cities.append(city)
    print("Город добавлен.")

def remove_record(cities):
    """Удалить словарь с данными о городе из списка."""
    name = input("Какой город удалить? ").strip().lower()
    for city in cities:
        if city["name"].lower() == name:
            cities.remove(city)
            return
    print("Не удалось найти город.")

def find_record(cities):
    """Поиск записи по названию города."""
    name = input('Введите название: ').strip().lower()
    found = [c for c in cities if name in c['name'].lower()]
    print_result(found)

def sort_and_filter(cities):
    """Сортировка и фильтрация."""
    print('1. Сортировка по населению (возр.)')
    print('2. Сортировка по населению (убыв.)')
    print('3. Фильтр по стране')
    print('4. Фильтр по населению (больше N)')
    choice = input('Выбор: ').strip()

    if choice == '1':
        print_result(sorted(cities, key=lambda c: c['population']))
    elif choice == '2':
        print_result(sorted(cities, key=lambda c: c['population'],
                            reverse=True))
    elif choice == '3':
        country = input('Страна: ').strip().lower()
        print_result([c for c in cities if c['country'].lower() == country])
    elif choice == '4':
        n = int(input('Население больше: '))
        print_result([c for c in cities if c['population'] > n])
    else:
        print('Неизвестная команда.')

def print_result(cities):
    """Вывод для результатов поиска, сортировки и фильтрации."""
    if not cities:
        print('Ничего не найдено.')
        return
    print(f"{'Наименование':<15}{'Год':<8}{'Население':<15}{'Страна'}")
    print('-' * 50)
    for c in cities:
        print(f"{c['name']:<15}{c['year']:<8}{c['population']:<15}{c['country']}")

def main():
    cities = load_records()
    print(f"Загружено записей о городах: {len(cities)}")

    while True:
        print("\n=== МЕНЮ ===")
        print("-" * 50)
        print("1. Показать записи")
        print("2. Добавить запись о городе")
        print("3. Удалить запись о городе")
        print("4. Найти запись о городе")
        print("5. Сортировка / фильтрация")
        print("6. Сохранить в файл .csv")
        print("0. Выход")

        choice = input('Выбор: ').strip()
        if choice == '1':
            print_result(cities)
        elif choice == '2':
            add_record(cities)
        elif choice == '3':
            remove_record(cities)
        elif choice == '4':
            find_record(cities)
        elif choice == '5':
            sort_and_filter(cities)
        elif choice == '6':
            save_records(cities)
            print('Сохранено в', FILE)
        elif choice == '0':
            save_records(cities)
            print('Данные сохранены. Выход.')
            break

if __name__ == '__main__':
    main()
