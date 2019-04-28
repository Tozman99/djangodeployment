import os 

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Success_project.settings')

import django 

django.setup()

import random 
from Success_App.models import User 
from faker import Faker 


fakegen = Faker()


def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name = fake_first_name,last_name= fake_last_name,email=fake_email)[0]


if __name__ == '__main__':
    print('complete')
    populate(10)
    print('COMMPLETE')
