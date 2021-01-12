# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         celery_config
# Description:  
# Author:       Allen
# Time:         2021/1/12 14:02
# ------------------------------------------------------------------------------
from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
    'celery_study.task_add'
)

CELERYBEAT_SCHEDULE = {
    # 每10s执行一次
    'task1': {
        'task': 'celery_study.task_add.add',
        'schedule': timedelta(seconds=10),
        'args': (2, 8)
    },
    # 每天15:00执行
    'task2': {
        'task': 'celery_study.task_add.add',
        'schedule': crontab(hour=15, minute=0),
        'args': (9, 9)
    }
}
