from django.apps import AppConfig


class SenderConfig(AppConfig):
    name = 'fabric_test'

    def ready(self):
        from fabric_solution import sender_scheduler
        sender_scheduler.start()
