# my_kinosite_project - requirements
Library Django v4.1.6,
Library Pillow v9.4.0,
Django CKEditor v6.5.1



ИНСТРУКЦИЯ ПО ЗАПУСКУ:

Склонировать проект: https://github.com/Nazar-Smile/my_kinosite_project.git
Перейти по пути, где расположены основные файлы включая manage.py: cd my_kinosite_project
Установить библиотеку для работы с виртуальным окружением и пакетами(Если не установлено): sudo apt install python3-pip а затем sudo apt install python3-pip
Создать виртуальное окружение: python3 -m venv env
Активировать виртуальное окружение: source env/bin/activate
Установить библиотеки для работы приложения из requiremts.txt: pip install -r requirements.txt
Подготовить и проихвести миграции: python3 manage.py makemigrations далее  python3 manage.py migrate
Создать суперпользователя: python3 manage.py createsuperuser
Войти на страницу админа http://127.0.0.1:8000/admin/ и добавить фильм
