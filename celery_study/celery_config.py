# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         celery_config
# Description:  
# Author:       Allen
# Time:         2021/1/12 14:02
# ------------------------------------------------------------------------------


BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
    'celery_study.task_add'
)
