
import os
DEBUG = True
SECRET_KEY = 'very-secret-key-for-temp-use'
INSTALLED_APPS = [
    '__main__.MyappConfig', # Refers to the MyappConfig defined in the notebook's global scope
]
# ROOT_URLCONF will point to this temporary settings module itself,
# assuming urlpatterns are also defined in the notebook's global scope.
ROOT_URLCONF = 'temp_settings_jupyter'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]
