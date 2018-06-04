# CryptoCurrencyAdvertisement

# Setup initialize commands
install pipenv
```
brew install pipenv
```
OR
```
pip3 install pipenv
```

install packages
```
pipenv install
```

upgrade pip
```
python3 -m pip install --upgrade pip
```
install django
```
pipenv install django
```
if update django
```
pipenv update django
```
init django(create project)
```
django-admin startproject cca
```
run django server
```
python3 manage.py runserver
```

# Setup MySQL database commands
migrate django
```
python3 manage.py migrate
```
use and connect mysql
install PyMySQL
```
pipenv install PyMySQL
```
and edit settings.py like this
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crypto_currency_advertisment',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
and edit manage.py to add next to "import sys", add the following two lines.
```python
import pymysql
pymysql.install_as_MySQLdb()
```
check the django can connect mysql and migrate.
```
python3 manage.py migrate
```

# Setup Application(Controllers and views)
create apps(It is controller and view)
```
python3 manage.py startapp adnem
```
edit adnem/views.py like this.(This is a controller)
```
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")
```

edit adnem/urls.py like this.(This is a routing)
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

edit cca/urls like this.(This is a project routing)
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('adnem/', include('adnem.urls')),
    path('admin/', admin.site.urls),
]
```

# Setup and controll database migration

Create migration file from the models.
```
python3 manage.py makemigrations adnem
```
If you want to change table configuration, you edit this file made by above.

Migrate only application and version.
```
python3 manage.py sqlmigrate adnem 0001
```

Migrate all tables
```
python3 manage.py migrate
```

Drop all tables.
```
python3 manage.py migrate adnem zero
```