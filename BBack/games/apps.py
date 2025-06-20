from django.apps import AppConfig


class GamesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "games"
    verbose_name = "Игры"

    def ready(self):
        from . import life_cycle
        life_cycle.run_lc()