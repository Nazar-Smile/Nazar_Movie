# my_kinosite_project


Цель проекта сайт для просмотра фильмов, на сайте реализовано много функционала, таких как аутентификация, просмотр фильмов, трейлеров, кадров к фильмам, актеров, добавление комментариев и прочего.


ИНСТРУКЦИЯ ПО ЗАПУСКУ:

Склонировать проект: https://github.com/Nazar-Smile/my_kinosite_project.git
Перейти по пути, где расположены основные файлы включая manage.py: cd my_kinosite_project
Установить библиотеку для работы с виртуальным окружением и пакетами(Если не установлено): sudo apt install python3-pip а затем sudo apt install python3-pip
Создать виртуальное окружение: python3 -m venv env
Активировать виртуальное окружение: source env/bin/activate
Установить библиотеки для работы приложения из requiremts.txt: pip install -r requirements.txt
Подготовить и произвести миграции: python3 manage.py makemigrations далее  python3 manage.py migrate
Создать суперпользователя: python3 manage.py createsuperuser
Войти на страницу админа с новым пользователем http://127.0.0.1:8000/admin/ и добавить фильм
