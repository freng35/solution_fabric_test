from django.db import models
from django.db.models import Count


class Client(models.Model):
    client_id = models.IntegerField(unique=True)
    phone_number = models.CharField(max_length=11)
    operator_code = models.IntegerField()
    tag = models.IntegerField()
    time_zone = models.IntegerField()


class Mail(models.Model):
    mail_id = models.IntegerField(unique=True)
    date_start = models.DateTimeField()
    text = models.CharField(max_length=200)
    filter = models.IntegerField()
    date_end = models.DateTimeField()


class Message(models.Model):
    msg_id = models.IntegerField(unique=True)
    date_send = models.DateTimeField()
    status = models.CharField(max_length=100)
    mail_id = models.IntegerField()
    client_id = models.IntegerField()

    def as_json(self):
        return dict(
            msg_id=self.msg_id, date_send=self.date_send,
            status=self.status, mail_id=self.mail_id,
            client_id=self.client_id
        )
