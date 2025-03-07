import sys
from app_factory import create_celery
from config import get_settings

import warnings
warnings.filterwarnings("ignore")

import logging
import time

# 进行日志配置


celery = create_celery()

@celery.task
def add(x, y):
    return x + y

@celery.task
def mul(x, y):
    return x * y

@celery.task
def xsum(numbers):
    return sum(numbers)
