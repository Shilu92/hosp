from django.apps import AppConfig

class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'

    def ready(self):
        try:
            import dashboard  # Import to ensure Dash app is registered
        except ImportError:
            raise ImportError("Failed to import dash_apps module")