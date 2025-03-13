# Асинхронный парсер PEP

## Описание проекта
Данный проект представляет собой асинхронный парсер документов PEP, реализованный с использованием фреймворка Scrapy. Парсер собирает информацию о всех документах PEP с официального сайта [PEP](https://peps.python.org/) и сохраняет её в формате CSV.

## Установка и запуск

### 1. Клонирование репозитория
```bash
$ git clone https://github.com/VitsVi/scrapy_parser_pep.git
$ cd scrapy_parser_pep
```

### 2. Создание виртуального окружения и установка зависимостей
```bash
$ python -m venv venv
$ source venv/bin/activate  # Для Linux/Mac
$ venv\Scripts\activate    # Для Windows
$ pip install -r requirements.txt
```

### 3. Запуск проекта
Запуск паука:
```bash
(venv) $ scrapy crawl pep
```

## Структура проекта
```bash
scrapy_parser_pep
 ├── pep_parse/
     ├── spiders/
         ├── __init__.py
         └── pep.py
     ├── __init__.py
     ├── constants.py
     ├── items.py
     ├── middlewares.py
     ├── pipelines.py
     └── settings.py
 ├── results/
 ├── tests/
 ├── .flake8
 ├── .gitignore
 ├── README.md
 ├── pytest.ini
 ├── requirements.txt
 └── scrapy.cfg
```

## Функциональность
Парсер сохраняет информацию в два CSV-файла в директорию `results/`:

1. **pep_ДатаВремя.csv** – содержит список всех PEP:
   - `number` (номер PEP)
   - `name` (название PEP)
   - `status` (статус PEP)

2. **status_summary_ДатаВремя.csv** – содержит сводку по статусам PEP:
   - `Статус` (статус PEP)
   - `Количество` (количество PEP с этим статусом)
   - Последняя строка содержит `Total` и общее количество всех PEP

## Тестирование
Для запуска тестов выполните:
```bash
(venv) $ pytest
```

## Используемые технологии
- **Python 3.10+**
- **Scrapy**
- **CSV**

## Контакты
Автор: *VitsVi*
GitHub: [VitsVi](https://github.com/VitsVi)
Почта: Vits.Vi.08@yandex.ru
