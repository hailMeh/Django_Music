ЧАСТЬ 1 - НАЧАЛЬНАЯ УСТАНОВКА
----------------------------------------------------------------
1. Создается проект и application
2. Для Postgre устанавливается адаптер базы данных -> pipenv install psycopg2-binary
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
3. В данном проекте будет использоваться Bootstrap 5 -> docker-compose exec web pipenv install django-bootstrap-v5 . В settings регистрация
4. в pipfile вручную регистрация в packages -> django-bootstrap-v5 = "*", Тут возможно автоматом добавиться, docker-compose down и docker-compose up -d --build
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
1. В файле base.html внизу страницы создан код для правильного отображения данных из vue.js . На заметку! Также помнить про AJAX для джанго.гуглить.
-----------------------------------------------------------------
ЧАСТЬ 5 - ДОБАВЛЕНИЕ СТАТИКИ 
-----------------------------------------------------------------
1. В settings добавляется несколько строчек кода для правильного поиска для статических файлов в локальном виде и на продакшне.
2. В корне создается папка static и в ней css/js/images.
3. В base.html на самом верху указывается {% load static %} для загрузки всех статических файлов во всех шаблонах.
4. Для отображения изображения в шаблонах указывается тэг {% static 'images/name.jpg' %} 
5. Для использования js в скриптах указывается script src="{% static 'js/base.js' %}"><script>
6. Создадим еще одну страницу в pages app, она будет называться about. Создается шаблон, url, view, также прописываются ссылки из навбара.
7. В конце добавим тесты в pages  
8. В этой части мы добавили статические изображения, возможность использования js/vue кода и создали новую страницу about, также проверив всё тестами.
------------------------------------------------------------------
ЧАСТЬ 6 - ПРОДВИНУТАЯ РЕГИСТРАЦИЯ ЮЗЕРА / DJANGO ALLAUTH
------------------------------------------------------------------
1. Если после перерыва нам снова нужно запустить наш проект через докер - docker-compose up -d --build, после этого в контейнер будут загружен проект и все зависимости через pipfile и проект будет отображен по localhost.
2. Затем устанавливаем библиотеку для расширения представления регистрации юзера - docker-compose exec web pipenv install django-allauth, если использовать обычный pip,а не pipenv, то зависимости придется прописывать вручную. Через pipenv прописывается автоматом в Pipfile.
3. Затем сервер докера останавливается docker-compose down, и собирается заново docker-compose up -d --build. Так как появились новые библиотеки и проект нужно собрать заново.
4. затем необходимо прописать в settings.py новый установленный пакет 'allauth' и 'allauth.account'. Также укажем SITE_ID = 1 внизу.
5. Затем прописывается много строчек кода под новую библиотеку в файле settings.py, в основном заменяются дефолтные настройки и расширяется подкапотный функционал. Также меняются настройки редиректа при логине/логауте.
6. После внесенных настроек в setting.py нужно произвести миграцию docker-compose exec web python manage.py migrate
7. Затем в корневом urls.py меняется путь для user-management и удаляется строчка для регистрации в local-apps
8. Новая библиотека также будет смотреть на шаблоны представлений для регистрации и авторизации в папке templates, как и в дефолтных настройках. Но! дефолтные настройки смотрели в папку templates/registration/... . Django-allauth смотрит в папку templates/account/... . Так что создаем данную папку и переносим ранее созданные login.html и signup.html в неё. Папка registration более не нужна. Удалить!
9. Осталось поменять urls в ранее созданных файлах в путях шаблона _base.html. В ранее созданых путях {% url 'login'/logout/signup %} нужно подставить префикс 'account_ {% url 'account_signup' %}
10. Затем нужно создать новый шаблон для функции logout ->  templates/account/logout.html и немного поменять форму в actions.
11. В файле settings.py есть много настроек для логина/регистрации паользователя. Комментарии добавлены. Проверяем регистрацию, всё ли работает.
12. Тесты.
13. Allauth увеличил функционал регистрации и авторизации юзера, также добавив анимационные вставки при операции. Также можно использовать аккаунты из других популярных сайтов, гайд тут - https://django-allauth.readthedocs.io/en/latest/providers.html?highlight=naver.
14. Также в будущем в админке понадобится доступ к имени сайта - > для этого нужно прописать в settings в установленных приложениях -> 'django.contrib.sites',
15. Хорошая статья - https://russianblogs.com/article/6833594772/ . Показывает как подсоединить авторизацию через сервисы такие как гитхаб,гугл,эппл и много нужных вещей.
-----------------------------------------------------------------
ЧАСТЬ 7 - ФУНКЦИИ БЕЗОПАСНОСТИ
-----------------------------------------------------------------
1. Устанавливается пакет для усиленной защиты, в котором будут спрятаны секретные данные, такие как ключи проекта. docker-compose exec web pipenv install 'environs[django]'. После успешной установки пакета, docker-compose down и docker-compose -d --build.
2. Затем в settings.py импортируется from environs import Env, и прописывются две строчки пакета -> env = Env() , nv.read_env().
3. в docker-compose.yml прописывается новая строчка с секретным ключом. И в settings ключ прячится SECRET_KEY = env("DJANGO_SECRET_KEY"). Если секретный ключ будет содержать знак доллара $, то нужно поставить еще один такой знак, иначе будет ошибка - особенности докера.
4. Debug = True видим ошибки для разработчика. Спрячим его в env -> DEBUG = env.bool("DJANGO_DEBUG") и в docker-compose.yml -> 
5. В allowed host необходимо указать доступные для работы хосты - ALLOWED_HOSTS = ['community.pythonanywhere.com', 'localhost', '127.0.0.1']. Меняются в зависимости от конечного хостинга на котором будет распологаться сайт + локальный хост для работы.
6. Также спрячем базу данных в settings.py -> DATABASES = {
    "default": env.dj_db_url("DATABASE_URL", default="postgres://postgres@db/postgres")
}
7. На данном этапе благодаря установленный библиотеке environs, основные данные спрятаны в docker-compose.yml, который впоследствии также будет спрятан)))
-----------------------------------------------------------------
ЧАСТЬ 8 - ОТПРАВКА ПИСЕМ С САЙТА
-----------------------------------------------------------------
1. При успешной регистрации пользователя ему отправляется письмо с подтверждением его действий и приветствием на сайте! Используется библиотека allauth для такого функционала и чтобы изменить изначальный текст необходимо переписать несколько файлов.
2. Создадим два новых файла в папке templates/account/email/email_confirmation_subject.txt и templates/account/email/email_confirmation_message.txt и в них изменим изначальный текст нужный нам. Тут еще не забыть сделать migrate.
3. В админ панели будет указана строчка sites - в ней указанный шаблон example.com изменим на нужный нам.
4. Внизу settings укажем строчку -> DEFAULT_FROM_EMAIL = 'admin@djangomusic.com'
5. Теперь пользователю будет отправлено сообщение от указанного email и с новым названием сайта. Но пока что только в логах :)
6. При отправке пользователю сообщения ему также будет предоставлена ссылка для подтверждения при переходе по которой он получит шаблон страницы с подтверждением.
	Для красивого отображения нового шаблона его нужно создать в месте где распологаются все allauth шаблоны -> templates/account/email_confirm.html. Шаблон будет 	   отличаться от предыдущих, так что взять из репозитория.
7. Также для будущих манипуляций с аккаунтом, стоит сразу добавить два шаблона c путями url -> templates/accounts/password/reset/  -> templates/accounts/password/change/ и accounts/password/reset/done/. Подробнее по ссылке - https://russianblogs.com/article/6833594772/.
8. После созданных шаблонов как пример подключаемся к внешнему smtp серверу smtp.mail.ru. В settings указываем порт,хост и юзера. Пример в файле. Для аналогов почтовых сервисов по ссылке - https://vivazzi.pro/ru/it/send-email-in-django/
9. В данном разделе полностью настроена работа с почтовым клиентом для сброса/восстановления пароля.
-----------------------------------------------------------------
ЧАСТЬ 9 - Добавление списка обьектов, определенный обьект, защищенный URL, удаление и создание базы данных.
-----------------------------------------------------------------
1. Создадим новый app docker-compose exec web python manage.py startapp music. И зарегистрируем его в settings.
2. Далее в новом приложении music/models.py создадим новую модель данных. docker-compose exec web manage.py makemigrations и migrate. Регистрация в админке.
3. СОздается новый url файл в приложении,а в корневом url указывается include.
4. В файле views создается новое представление для отображения данных в модели -> ListView 
5. Затем создается шаблон для представления в templates/music/music_list.html и происходит отображение всех обьектов в модели music.
6. Если можно посмотреть все модели,то значит можно и определенную. Для этого создается новый url с <int:pk> в music/urls и во views используется DetailView. Для перехода к определенному обьекту из списка всех альбомов, создается кнопка с ссылкой {% url 'music_detail' m.pk %}. Тут в качестве pk используется уникальный ключ обьекта. Впоследствии лучше использовать slug, так как он более гибок в названии, можно использовать и строчки и цифры.
7. Также принято использовать get_absolute_url для получения определеннго обьекта. В модели music импортируется reverse и используется у модели Music в качестве метода. При использования slug, код будет отличаться, смотреть в  репозитории Django-Books. После добавления реверса меняются ссылки в шаблонах с {% url 'music_detail' m.pk %} на {{ m.get_absolute_url }}. Данный метод более гибок,так как позволяет смотреть обьект из админки и обладает более защищенным от ошибок отображением обьекта. Юзать его.
8. Также для лучшей защиты от хакерских атак лучше использовать - uuid. В моделях импортируется uuid и прописывается в поле id с параметрами. В music/urls меняется путь на <uuid:pk>. База данных была изменена и в данной ситуации единственный выход это удалить базу с музыкой docker-compose exec web rm -r music/migrations -> docker compose down. Для проверки созданных баз -> docker volume ls. Так как использовать postgre нужно будет удалить архив docker volume rm music_postgres_data -> docker-compose up -d -> docker compose exec web python manage.py makemigrations music -> docker compose exec web python manage.py migrate -> docker compose exec web python manage.py createsuperuser. В данном случае мы удалили полностью базу данных и пользователей и создали заново. Продумать базу лучше заранее во избежании подобных ситуаций!
9. В данном разделе мы расширили функционал сайта списком композиций и одной определенной, добавили защищенные пути URL и заново собрали базу данных после критических изменений.
-----------------------------------------------------------------
ЧАСТЬ 10 - FOREIGN KEYS RELATIONSHIP, РЕЦЕНЗИИ ПОЛЬЗОВАТЕЛЕЙ К АЛЬБОМАМ 
-----------------------------------------------------------------
1. Создадим возможность пользователям оставлять свои рецензии к альбомам. Для этого в ранее созданом music app создадим новую модель, в которой поле album будет связано с моделью Music и поле author будет автоматически использоваться для авторизованного пользователя. app docker-compose exec web python manage.py makemigrations music -> docker-compose exec web python manage.py migrate
2. Затем в админке music/admin прописывается TabularInline класс для основной модели Music, для того чтобы отображение рецензий было сразу видно из модели Music в админке. Для теста создадим юзера и через админку пропишем несколько рецензий для будущего их отображения.
3. На данном этапе создана связь между одним альбомом и рецензиями к ней. Чтобы отобразить данные рецензии к альбому в шаблоне перейдем в music_detail.html и в нужном месте пропишем цикл for, который будет брать рецензии из music.reviews.all(т.е из альбома берутся все рецензии через related name(имзмененное имя)) и затем отображаются также как в обычном цикле.
4. В будущем в этот раздел еше добавится инструкция по добавлению своих рецензий через форму. Возможно через Vue.
-----------------------------------------------------------------
ЧАСТЬ 11 - Загрузка собственных изображений на сайт
-----------------------------------------------------------------
1. Для возможности загрузки пользовательских изображений и файлов нам необходимо установить библиотеку pillow -> docker-compose exec web pipenv install pillow -> docker-compose down -> docker-compose up -d --build.
2. Затем в settings добавим две строчки MEDIA_URL -> MEDIA_ROOT и создадим новую попку в корне проекта media и в ней media/covers.
3. В файле config/urls импортируется два модуля и пишется строчка кода с загрузкой статики. В файле пометка # images.
4. Для загрузки изображений нужно добавить соответствующее поле в модель Music. Для изображений ImageField, для обычных файлов - FileField. Затем docker-compose exec web python manage.py makemigrations music -> docker-compose exec web python manage.py migrate
5. Теперь если зайди в админку и попробовать загрузить изображение, то оно автоматически загрузится в проект в ранее созданную папку media/covers
6. Чтобы отобразить изображение в шаблоне необходимо для src указать => src="{{ music.cover.url }}. И сделаем защиту от альбомов у которых нету изображения условием if music.cover. Также для новых картинок можно установить ссылку по нажатию через ранее созданный get_absolute_url.
7. В будущем добавим возможность добавлять свои альбомы и загружать свои изображения через форму, смотрим в Django_books.
-----------------------------------------------------------------
ЧАСТЬ 12 - Добавление альбомов пользователем
-----------------------------------------------------------------
1. Чтобы пользователь мог добавлять свои собственные альбомы, необходимо создать форму для этого. Начнем с установки библиотеки docker-compose exec web pipenv install django-simple-captcha. Добавляем в setting в 3rd party app и делаем перестройку контейнера docker-compose down -> docker-compose up -d --build. Также необходимо сделать миграцию. Также не забыть в корне path('captcha/', include('captcha.urls')). Подробно по этой библиотеке https://django-simple-captcha.readthedocs.io/en/latest/advanced.html. Капча нужна. Защиты прибавляет.
2. Затем создаем форму в music/forms.py и прописываем путь для отображения новой формы в urls.
3. Во views импортируем CreateView, добавляем к классу форму и reverse_lazy. Также добавим миксин что только авторизованный пользователь может добавлять альбомы иначе доступ будет запрещен.
4. Создаем новый шаблон templates/music/add_music.html, добавляем новую форму и проверяем.
5. Также в данном разделе можно еще сделать отображение более удобных для пользователя отображение ошибок, таких как доступ запрещен и страница не найдена. Для этого в корневом urls пропишем handler403 = authNeed, данные хэндлеры будут обработчиками событий ошибок и направлять на нужный шаблон с сообщением. Из music.views будет импортирована функция authNeed в которой будет происходить обработка ошибок и содержаться шаблон для показа.
-----------------------------------------------------------------
ЧАСТЬ 13 - Миксины для доступа к CRUD только определенным пользователям.
-----------------------------------------------------------------
1. На данном этапе любой пользователь может добавлять альбомы, независимо авторизирован он или нет. Надо это исправить. Для начала в music/views импортируем LoginRequiredMixin, который будет давать доступ для просмотра и добавления альбомов только авторизованным пользователям.
2. Затем данный миксин добавляется к классам в которых мы хотим поставить запрет на посещение страница. В данной ситуации запрет будет указан у всех трех ранее созданных классов. При функциональных представлениях используются декораторы. В нашем случае миксины.
3. Также необходимо поставить редирект для класса после успешного запрета. Можно использовать success_url или login_url в которых будет указан шаблон для редиректа. Reverse_lazy для редиректа в последнюю очередь после успешной обработки всех остальных событий.
4. Затем создадим в админке нового пользователя. Здесь также можно указать свою группу с разрешениями для определенных пользователей. Но в целях обучения создадим свои собственные. Для этого в модели Music необходимо указать класс Meta, в котором мы создадим новое разрешение и оно отобразится в разрешениях пользователя в админке, также надо сделать миграции.
5. Теперь в view импортируем новый миксин, который запрашивает разрешение и применим его к DetailView. Теперь пользователь без данного разрешения не сможет смотреть детально альбом. Но если ему это разрешение предоставить через админку, то просмотр будет разрешен.
6. Также в будущем для более глубокого изучения разрешенного доступа можно погуглить Добавление пользователей в определенные группы со своими разрешениями, например премиум-аккаунты. Также присутствуют еще один популярный миксин UserPassesTestMixin.
-----------------------------------------------------------------
ЧАСТЬ 13 - ПОИСК В БАЗЕ И ПОКАЗ РЕЗУЛЬТАТА В ШАБЛОНЕ.
-----------------------------------------------------------------
1. Для создания поиска нам необходимо создать view/url/template для показа результата. Начнем с создания url в music/urls, затем создадим новый класс представления который будет иметь ListView и шаблон для показа результатов search_results.html. Весь этап аналогичен простому представлению обьектов в модели через for.
2. Основа есть, queryset = Music.objects.filter(title__icontains='Bell') дефолтный ListView будет изменен и станет показыватьь только обьекты у которых title имеет строку Bell. Но нам нужно чтобы пользовательский поиск выдавал нужный результат. Для этого в home.html пропишем новую форму, в котором будет находиться input. И после того как Пользователь ввел нужный ему текст будет выдаваться результат. Во view меняется queryset.
3. Django-watson и django-haystack предлагают более расширенные настройки для работы с поиском, по необходимости гуглить.
-----------------------------------------------------------------
ЧАСТЬ 14 - ОПТИМИЗАЦИЯ РАБОТЫ САЙТА, PERFOMANCE. Cache, Index.
-----------------------------------------------------------------
1. Для начала оптимизации сайта необходимо установить библиотеку docker-compose exec web pipenv install django-debug-toolbar и затем остановить контейнер docker-compose down. После установки надо зарегистрировать установленную библиотеку в settings -> debug_toolbar. Также необходимо внести изменения в настройку MIDDLEWARE - > смотреть в файле setting. И третья настройка - INTERNAL_IPS, если докер не используется то указать INTERNAL_IPS = '127.0.0.1', в случае использования докера необходимо ипортировать библиотеку socket и написать две строчки кода -> смотреть в файл. После данных манипуляций тулбар готов к использованию -> docker-compose up -d --build.
Также, чтобы тулбар показывался только в DEBUG = True методе нужно прописать строчку в корневом url.
2. Затем добавим кэш. У джанго есть встроенная функция для кэширования, также как альтернатива присутствуют библиотеки Memcached и django-redis. Самый удобный способ кэша, это добавления в settings кода, который будет указывать где кэш будет храниться, затем в нужном шаблон загружается {% load cache %} и нужный нам фрагмент кода который не меняется оборачивается тэгом {% cache 20 sidebar %} -> Где cache указание функции, 20 -> время кэша -> sidebar для удобства обозначения оборачиваемого кода.
3. Также для ускорения считывания данных из базы можно применить индексирования для модели. Плюсы - приблизительное ускорение считывания на 25%, минусы - затраты на обьем требуемой памяти в жестком диске увеличиваются. Для этого надо добавить в music/models в модель Music -> db_index = True к полю id или всем другим полям и сделать миграции.
4. Для ускорения работы django ORM также можно использовать 3rd party package - django-extensions. Гуглить.
5. Также для уменьшения размеров статических файлов,таких как изображения могут использоваться такие пакеты как django-compressor и easy-thumbnails.
-----------------------------------------------------------------
ЧАСТЬ 15 - Безопасность.
----------------------------------------------------------------
1. 
