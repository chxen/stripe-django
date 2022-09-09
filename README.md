# stripe-django
Настройка платежей Stripe с помощью Django

## Описание запуска
1) Cклонируйте репозиторий командой: git clone https://github.com/chxen/stripe-django.git
2) Зайдите в папку cd stripe-django
3) Создайте виртуальное окружение: python -m venv venv. И активируйте его: source venv/bin/activate
4) Установите необходимые зависимости из файла requirements.txt: pip install -r requirements.txt
5) Перейдите в папку project и выполните миграции: python manage.py makemigrations, python manage.py migrate
6) Запустите проект на сервере: python manage.py runserver
7) Чтобы получить доступ к панели администратора, создайте суперпользователя: python3 manage.py createsuperuser. Введите необходимые данные и запомните их. Они понадобятся для того, чтобы войти в Django Admin панель. Там можно просмотреть Django Модели.

## Задачи
- [X] Django Модель Item с полями (name, description, price) Ссылка: http://ksenih.pythonanywhere.com/admin/
- [X] GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса Ссылка: http://ksenih.pythonanywhere.com/buy/1/
- [X] GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id) Ссылка: http://ksenih.pythonanywhere.com/item/3/
- [X] Залить решение на Github, описать запуск в Readme.md
- [X] Опубликовать свое решение чтобы его можно было быстро и легко протестировать. Ссылка: http://ksenih.pythonanywhere.com
- [ ] Запуск используя Docker
- [X] Использование environment variables
- [X] Просмотр Django Моделей в Django Admin панели Ссылка: http://ksenih.pythonanywhere.com/admin/
- [X] Запуск приложения на удаленном сервере, доступном для тестирования Ссылка: http://ksenih.pythonanywhere.com
- [ ] Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
- [ ] Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 
- [ ] Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
- [ ] Реализовать не Stripe Session, а Stripe Payment Intent.
