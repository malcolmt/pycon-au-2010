import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SITE_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(SITE_DIR, "phm.sqlite"),
        #"NAME": "/home/malcolm/tmpfs/phm.sqlite",
    }
}

TIME_ZONE = "Australia/Sydney"

SITE_ID = 1

# Make this unique, and don"t share it with anybody.
SECRET_KEY = "y$2!w=_bo-owlf8^@w$$@10*aywwi9thfi0!9+=-rbc=ic5-nm"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
)

ROOT_URLCONF = "phm_urls"

TEMPLATE_DIRS = (
    # Don"t forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.admin",
    "phm_collection",
)

FIXTURE_DIRS = [os.path.join(SITE_DIR, "fixtures")]

