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

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        #get the topic
        top = add_topic()

        #create the fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name =  fakegen.company()

        #entry for webpage
        webpage = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

        #fake acess record for the web page 
        access_record = AcessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('population complete')
