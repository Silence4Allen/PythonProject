# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         __init__.py
# Description:  
# Author:       Allen
# Time:         2021/1/12 13:27
# ------------------------------------------------------------------------------
from celery import Celery

app = Celery('demo')
# 通过celery实例获取配置
app.config_from_object('celery_study.celery_config')
