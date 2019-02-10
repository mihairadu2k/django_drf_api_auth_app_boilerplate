# Django Backend

## Create the virtual enviroment and install requirements.txt file if it exists.

```shell
$ python -m venv src
$ .\src\Scripts\activate
  ---or---
$ source .\src\bin\activate

  ---if exists the requirements file---
$ (src) pip install -r requirement.txt

  '--- if not existing ---'

$ pip install pytz Django django-cors-headers django-countries django-filter django-templated-mail djangorestframework PyJWT djoser Markdown Pillow python-dotenv

#!! JWT is changed to the Simple JWT
  '--- for MSSQL --- '

$ pip install pyodbc django-pyodbc-azure

  '--- for PostgreSQL ---'
$ pip install psycopg2-binary
```

## Create the DJANGO Project:

```shell
  django-admin startproject backend_api
```

### Setting up the **_settings.py_** file:

a) adding the apps to installed apps array:

- CORS: https://github.com/OttoYiu/django-cors-headers
- DRF: https://www.django-rest-framework.org/
- AUTH - DJOSER: https://djoser.readthedocs.io/en/stable/
- AUTH - DRF Simple JWT:https://github.com/davesque/django-rest-framework-simplejwt
- DJANGO - GUARDIAN: https://django-guardian.readthedocs.io/en/stable/installation.html
```python
import datetime
INSTALLED_APPS = [
    ...,
  'rest_framework',
  'rest_framework.authtoken',
  'djoser',
  'corsheaders',
]
MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]
CORS_ORIGIN_WHITELIST = (
      'localhost:8000',
      'localhost:8080', # the front server
)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

SIMPLE_JWT = {
    # 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1), # DEV MODE
    # 'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=2), # DEV MODE
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,


}
```

b) adding the **.env** file

- python-dotenv: https://github.com/theskumar/python-dotenv

```docs
  .
  ├── .env
  └── settings.py
```

```python

# settings.py
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity:
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

#wsgi.py and manage.py
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

```

c) setting up the database:

  * MSSQL
```python
DATABASES = {
    'default': {
        'ENGINE'  : 'sql_server.pyodbc',
        'HOST'    : 'DESKTOP-C6RS3DO',
        'NAME'    : 'demo2016',
        'USER'    : 'sa',
        'PASSWORD': 'sa',
        'PORT'    : '',
#        'OPTIONS' : {
#           'driver': 'ODBC Driver 13 for SQL Server',
#      },
    }
}
```

* Setting up multiple DATABASES:
DATABASE_ROUTERS = ['path.to.demoRouter']

d) Setting up the **api_auth** app
	* add it to **settings.py**
	* add the **urls.py** file and configure the path for djoser urls.
	
```python
from django.urls import include, path
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.token')),
    ]
```
  * creating a new user model extending the user model and replacing it in **settings.py**
	 info: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html

```python
#settings.py
AUTH_USER_MODEL = '<app containing the user profile>.<User model name>'
```
  * updating the serializer classes for the DJOSER views (user and current user) so the fields we add to the model are 
  available.
---	




### Documentation:
[OPNE API DRF]: 
	* https://drf-yasg.readthedocs.io/en/stable/readme.html#installationDR

### FUTURE RESEARCH

#### LINKS:

1. [auth0]: 
	* https://auth0.com/docs/quickstarts
2. [search]: 
	* https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html
3. [REST Serializer]s: 
	* https://dynamic-rest.readthedocs.io/en/latest/tutorial.html #NOT WORKING
4. [Boilerplate]: 
	* https://github.com/gtalarico/django-vue-template
5. [TastyPie]: 
	* https://django-tastypie.readthedocs.io/en/latest/tutorial.html#configuration
6. [The AJAX Requests from the front-end - CSRF]:
 	* https://www.django-rest-framework.org/topics/ajax-csrf-cors/
	* https://stackoverflow.com/questions/35881201/django-rest-framework-csrf-and-vue-js
7. [Testing in Django]: 
	* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
8. [Static files in Django]: 
	* https://docs.djangoproject.com/en/2.1/howto/static-files/	
9. [DRF Multile Models in Same View]:
	* https://github.com/MattBroach/DjangoRestMultipleModels
10. [Interesting approach of JWT Logout MUST SEE]:
	* https://tag1consulting.com/blog/building-api-django-20-part-i
11. [PACKAGES]:
	* https://djangopackages.org/
12. [DJ Pandas]:
	* https://django-pandas.readthedocs.io/en/stable/
13. [Multiple Models]:
	* https://github.com/MattBroach/DjangoRestMultipleModels
#### BOOKS: 

0.  [Beginning DJANGO]: 
	* https://www.webforefront.com/django/
1.  [Django ORM Cookbook]: 
	* https://books.agiliq.com/projects/django-orm-cookbook/en/latest/index.html
2.  [Django DRF Cookbook]: 
	* https://books.agiliq.com/projects/django-api-polls-tutorial/en/latest/
3.  [Django Multiple Tenants Cookbook]: 
	* https://books.agiliq.com/projects/django-multi-tenant/en/latest/index.html
4. [Python tips and tricks]:
	* http://book.pythontips.com/en/latest/args_and_kwargs.html
		
### RECURENT PROBLEMS:
1. [in the create methods (CreateAPIView) requests.POST and requests.GET are immutable. Here is a trick to make them mutable]: https://stackoverflow.com/questions/44717442/this-querydict-instance-is-immutable
