import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()


from faker import Faker
from first_app.models import AccessRecord, Topic, Webpage, User
import random


fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'news', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # Create  the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.name()

        fake_user_name= fakegen.name().split()
        fake_first_name = fake_user_name[0]
        fake_last_name = fake_user_name[1]
        fake_email = fakegen.email()

        # create the new webpage entry
        user = User.objects.get_or_create(first_name = fake_first_name, last_name=fake_last_name, email=fake_email)[0]
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

        return acc_rec



if __name__ == '__main__':
   print('populating script!')
   populate(20)
   print('populating complete!')


