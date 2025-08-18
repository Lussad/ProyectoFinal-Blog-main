from .base import * 

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR_STR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR_STR, 'media')

DEBUG = False

ALLOWED_HOSTS = []

SECRET_KEY = ''


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'carrito$carrito',  # formato: usuario$nombre_basedatos
        'USER': '',
        'PASSWORD': '',
        'HOST': 'carrito.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
