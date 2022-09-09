# stripe-django
Настройка платежей Stripe с помощью Django

1) Cклонируйте репозиторий командой: git clone https://github.com/chxen/stripe-django.git
2) Зайдите в папку cd stripe-django
3) Создайте виртуальное окружение: python -m venv venv. И активируйте его: source venv/bin/activate
4) Установите необходимые зависимости из файла requirements.txt: pip install -r requirements.txt
5) Перейдите в папку project и выполните миграции: python manage.py makemigrations, python manage.py migrate
6) Запустите проект на сервере: python manage.py runserver
7) Чтобы получить доступ к панели администратора, создайте суперпользователя: python3 manage.py createsuperuser. Введите необходимые данные и запомните их. Они понадобятся для того, чтобы войти в Django Admin панель. Доступ по ссылке: http://127.0.0.1:8000/admin/. Там можно просмотреть Django Модели.

