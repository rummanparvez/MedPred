from django.apps import AppConfig

class MainAppConfig(AppConfig):
    name = 'main_app'
    default_auto_field = 'django.db.models.BigAutoField'  # Add this line
