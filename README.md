# CryptoCurrencyAdvertisement

# Command
init python vertual env
```
python3 -m venv CryptoCurrencyAdvertisement
```
start virtual env
```
source CryptoCurrencyAdvertisement/bin/activate
```
upgrade pip
```
python3 -m pip install --upgrade pip
```
install django
```
pip3 install django
```
if update django
```
pip3 install django -U
```
init django
```
django-admin startproject cca
```
run django server
```
python3 manage.py runserver
```
migrate django
```
python3 manage.py migrate
```
use and connect mysql
install PyMySQL
```
pip3 install PyMySQL
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