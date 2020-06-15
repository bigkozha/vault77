DEBUG = True
SECRET_KEY = 'SECRET'
ROOT_URLCONF = 'urls'

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.sqlite3',
        'NAME' : 'counter.db',
    }
}

INSTALLED_APPS = [
    'counter'
]