DEBUG = True

DATABASES = {
    "default": {
       'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'market',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_WHITELIST = []

SITE_URL = "http://127.0.0.1:8000/"