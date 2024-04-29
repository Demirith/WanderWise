from .settings import *  # Import base settings from settings.py

# Overriding the DATABASES setting for tests to use SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Using a file-based SQLite database
    }
}

# Disable caching during tests
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# Set a flag for testing
TESTING = True

# Optionally disable middleware that might interfere with tests
# or aren't necessary for test execution
MIDDLEWARE = [mw for mw in MIDDLEWARE if mw not in [
    'django.middleware.csrf.CsrfViewMiddleware',  # Example: Disable CSRF in tests
]]

# If you use email in your application, redirect emails to a dummy backend during tests
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Reduce password hashing time for faster test execution
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
