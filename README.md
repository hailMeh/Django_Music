ЧАСТЬ 1 - НАЧАЛЬНАЯ УСТАНОВКА
----------------------------------------------------------------
1. Создается проект и application
2. Для Postgre устанавливается адаптер базы данных -> pip install psycopg2-binary
3. В корне создаются два файла для докера - Dockerfile и docker-compose.yml
4. Сервер останавливается и запускается консоль - > в корень проекта -> docker-compose up -d(для сохранения возможности работы при включенном сервере) --build(сразу в одну строку и build контейнера)
5. В проекте в settings устанавливается database PostgreSQL
6. Изначальная установка проекта + докер + база данных настроены.

----------------------------------------------------------------
ЧАСТЬ 2 - ИЗМЕНЕНИЕ стандратной модели юзера Джанго
-----------------------------------------------------------------
1. Создаем новый app для аккаунтов юзеров через докер -> docker-compose exec web python manage.py startapp accounts
2. В созданном app в моделях создаётся новая модель, которая будет расширять функционал базы
3. В settings регистрируется новый app И в самом низу пишется AUTH_USER_MODEL = 'accounts.CustomUser', которая будет заменять дефолтные значения
Makemigrations и migrate в консоли докера.
4. В accounts создается forms.py в котором будет созданы формы для расширения дефолтных настроек аккаунта и для новых аккаунтов.
5. в accounts/admin.py добавляется новая модель юзера и формы для представления в админке.
6. Создаем суперюзера docker-compose exec web python manage.py createsuperuser
7. Для проверки правильной настройки на данном этапе в accounts/tests выполним проверку. Так как дефолтные настройки были изменены, на данном этапе следует это сделать. docker-compose exec web python manage.py test
8. Не забываем коммит и пуш в гит периодически.
9. На данном этапе мы изменили стандартную регистрацию и изменение форм для новых аккаунтов, в моделях создан CustomUser к которому можно добавлять новые поля. Также все отображается в админке

-----------------------------------------------------------------
ЧАСТЬ 3 - СОЗДАНИЕ СТРАНИЦ САЙТА
-----------------------------------------------------------------
1. Создаем новый app -> docker-compose exec web python manage.py startapp pages . Регистрация в settings
2. в корне -> папка templates -> создание базового шаблона base.html и создание новой папки pages в которой будет home.html
3. В данном проекте будет использоваться Bootstrap 5 -> docker-compose exec web pip install django-bootstrap-v5 . В settings регистрация
4. в pipfile вручную регистрация в packages -> django-bootstrap-v5 = "*"
5. Создание нового urls файла в pages app И его include из корневого url проекта. В нем первый path -> home
6. создание нового класса представление во views.py и отображение в нем созданного шаблона home.html
7. на данном этапе создан app для отображения страниц, базовый шаблон, главная страница.

------------------------------------------------------------------
ЧАСТЬ 4 - РЕГИСТРАЦИЯ ЮЗЕРА
------------------------------------------------------------------
1. В проекте в файле url создается новый path для манипуляций с авторизацией и регистрацией юзеров
2. в шаблоне base.html в навбаре указывается jinja2 метод {% if user.is_authenticated %}
3. Джанго имеет встроенные пути для манипуляций с учётной записью - accounts/ -> login, logout, password_change,password_reset. Если в шаблоне при нажатии на кнопку указать путь 'accounts/logout', то юзер автоматически выйдет из учетной записи. Для login уже нужно будет создать шаблон.
4. Для аторизации пользователей нужна форма для ввода данных и шаблон внутри которого она будет храниться -> в templates создается папка registration, а в ней login.html. Папка registration является служебной, из нее автоматически(без прямой установки path в url) будут браться шаблоны, также со служебными именами.
5. Так как используется бутстрап, то хорошим дополнением к формам будет установка пакета - docker-compose exec web pip install crispy-bootstrap5 и регистрация зависимостей в settings. CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5" CRISPY_TEMPLATE_PACK = "bootstrap5". Не забывать прописывать их в pipfile.
6. Затем необходимо указать редирект при логине и логауте юзера, для этого в settings - LOGIN_REDIRECT_URL = 'home' LOGOUT_REDIRECT_URL = 'home'
7. В accounts app создаем urls.py. В нем будет прописан путь для регистрации пользователей signup. Также он include в корневом url
8. В accounts views создается класс для представления регистрации. В нем указана расширенная форма, шаблон и редирект при успешной регистрации.
9. В templates/registration/ создается шаблон signup.html для предоставления страницы при регистрации нового пользователя, также в base.html создается новая кнопка для регистрации, при нажатии на которую юзер автоматически попадает на созданный шаблон.
10. Желательно провести тесты для устранения больших проблем на позднем этапе. accounts/test.py
11. На данном этапе регистрация и авторизация юзера успешно созданы и протестированы. Регистрация берется из расширенной модели формы.
----------------------------------------------------------------
ДОП.МАТЕРИАЛ ПО VUE.JS 
----------------------------------------------------------------
1. В файле base.html внизу страницы создан код для правильного отображения данных из vue.js . На заметку!
-----------------------------------------------------------------
ЧАСТЬ 5 - ДОБАВЛЕНИЕ СТАТИКИ 
-----------------------------------------------------------------
1. 
