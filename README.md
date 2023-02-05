**Асинхронный парсер PEP**
==========================

Парсер документов PEP на базе фреймворка Scrapy.

**Описание**
============

-   Собирает номер, название и статус всех PEP.

-   Подсчитывает общее количество каждого статуса, а также общую сумму всех
    статусов.

Парсер собирает данные с сайта https://www.python.org/

Вся собранная информация сохраняется в файлах csv в папке results/...

**Как запустить проект**
========================

1.  Клонировать репозиторий:

>   [git\@github.com:vatut007/scrapy_parser_pep.git](git@github.com:vatut007/scrapy_parser_pep.git)

2.  Перейти в папку с проектом

cd scrapy_parser_pep

3.  Создать виртуальное окружение:

>   python -m venv venv

4.  Активировать виртуальное окружение, обновить версию pip и установить
    зависимости из requirements.txt:

source venv/bin/activate

python -m pip install -–upgrade pip.

pip install -r requirements.txt

5.  Запустить в консоле:

>   cd parser_pep

scrapy crawl pep
