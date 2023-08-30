# Example Settings

```
from django.conf import settings

settings.INSTALLED_APPS += [
    'dev_auth_backend',
]

settings.AUTHENTICATION_BACKENDS += ['dev_auth_backend.DevAuthBackend']
DEV_AUTH_BACKEND_PASSWORD = 'your_dev_password'
```