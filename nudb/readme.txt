Manual installation:
Python = 3 
Django==3.0.2
virtualenv==16.7.9
pytz==2019.3
Pillow==7.0.0
pyowm==2.10.0

            ******ckeditor******    https://pypi.org/project/django-ckeditor/ 

Install or add django-ckeditor to your python path.

\\1. pip install django-ckeditor
2. Add ckeditor to your INSTALLED_APPS setting.

***Перед тем как запустить команду collectstatic, необходимо в .settings.py
добавить строку STATIC_ROOT = os.path.join(BASE_DIR, 'static') и закомментить 
все строки связанные с 'static', затем переключить Debug в False. Запускаем команду 
python manage.py collectstatic - yes и возвращаем все как было в .settings.py.*** 



3. Run the collectstatic management command: $ ./manage.py collectstatic. 
This will copy static CKEditor required media resources into the directory 
given by the STATIC_ROOT setting. See Django’s documentation on managing 
static files for more info.



                *******schema_graph*******
\\1. pip install django-schema-graph
2. Add to .settings.py INSTALLED_APPS: 'schema_graph',
3. Add to your URLs.

from schema_graph.views import Schema
urlpatterns += [
    path("schema/" Schema.as_view()),
]

                *****django-admin-interface******
Installation
Run pip install django-admin-interface
Add admin_interface, flat_responsive, flat and colorfield to settings.INSTALLED_APPS
before django.contrib.admin
Run python manage.py migrate
Run python manage.py collectstatic
Restart your application server


psycopg2==2.8.4







Automatical installation:

altgraph==0.16.1
asgiref==3.2.3
astroid==2.3.3
attrs==19.3.0
autopep8==1.4.4
bandit==1.6.2
beautifulsoup4==4.8.2
certifi==2019.11.28
chardet==3.0.4
colorama==0.4.3
Django==3.0.2
django-admin-interface==0.12.0
django-ckeditor==5.9.0
django-colorfield==0.2.0
django-flat-responsive==2.0
django-flat-theme==1.1.4
django-freeze==0.6.4
django-grappelli==2.13.3
django-js-asset==1.2.2
django-schema-graph==0.0.2
future==0.18.2
geojson==2.5.0
gitdb2==2.0.6
GitPython==3.0.5
idna==2.8
isort==4.3.21
lazy-object-proxy==1.4.3
mccabe==0.6.1
pbr==5.4.4
pefile==2019.4.18
Pillow==7.0.0
psycopg2==2.8.4
pycodestyle==2.5.0
PyInstaller==3.5
pylint==2.4.4
pylint-django==2.0.13
pylint-plugin-utils==0.6
pyowm==2.10.0
pyTelegramBotAPI==3.6.6
pytz==2019.3
pywin32-ctypes==0.2.0
PyYAML==5.3
requests==2.22.0
six==1.13.0
smmap2==2.0.5
soupsieve==1.9.5
sqlparse==0.3.0
stevedore==1.31.0
urllib3==1.25.7
virtualenv==16.7.9
wrapt==1.11.2
xmltodict==0.12.0

