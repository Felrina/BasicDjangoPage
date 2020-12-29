import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

#FAKE POP script

import random
from first_app.models import AcessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ['news', 'markets', 'social', 'games', 'search']


