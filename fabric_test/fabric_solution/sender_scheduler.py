from apscheduler.schedulers.background import BackgroundScheduler

import sender.views


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(sender.views.check_time, 'interval', minutes=1)
    scheduler.start()