from django.apps import AppConfig


class FoodsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.foods'

    def ready(self):
        import apps.foods.signals

        return super().ready()
