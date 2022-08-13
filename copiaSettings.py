INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Clientes.apps.ClientesConfig",
    "Cuentas.apps.CuentasConfig",
    "Login.apps.LoginConfig",
    "Prestamos.apps.PrestamosConfig",
    "Tarjetas.apps.TarjetasConfig",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "itbank": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "itbank.sqlite3",
    },
}
