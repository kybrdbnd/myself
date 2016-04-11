from django.conf import settings
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False
DATABASES = settings.DATABASES
# STATICFILES_STORAGE = settings.STATICFILES_STORAGE
# Parse database configuration from $DATABASE_URL


DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
