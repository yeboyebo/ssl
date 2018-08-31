from os import path
import sys

PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))

sys.path.insert(0, path.join(PROJECT_ROOT, "../../../motor/"))
sys.path.insert(1, path.join(PROJECT_ROOT, "apps/"))

from YBAQNEXT.settings import *
from YBAQNEXT.yeboapps import *
from .local import *

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS += ('djangosecure', )
MIDDLEWARE_CLASSES += (
    'djangosecure.middleware.SecurityMiddleware',
)
