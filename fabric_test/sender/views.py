import datetime
from fabric_solution.models import *


def mailing_process(mail: Mail):
    clients = Client.objects.all()
    for client in clients:
        if client.tag == mail.filter or client.operator_code == mail.filter:
            print(Message.objects.all().count())
            msg_item = Message(
                date_send=datetime.datetime.now(tz=datetime.datetime.t),
                status="sent" if convert_to_datetime(mail.date_end) >= datetime.datetime.now() else "cancelled",
                mail_id=mail.mail_id,
                client_id=client.client_id,
                msg_id=Message.objects.all().count() + 1
            )
            msg_item.save()


def convert_to_datetime(dat):
    return datetime.datetime(
        dat.date().year, dat.date().month, dat.date().day,
        dat.time().hour, dat.time().minute, dat.time().second
        )


def check_time():
    mails = Mail.objects.all()
    for mail in mails:
        date_start = convert_to_datetime(mail.date_start)
        date_end = convert_to_datetime(mail.date_end)
        if date_start <= datetime.datetime.now() <= date_end:
            mailing_process(mail)
            mail.date_end = datetime.datetime.now()
            mail.save()
