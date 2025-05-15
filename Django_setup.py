import sys

import os

import django



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GameCenter.settings")

django.setup()
from data.models import  Genre