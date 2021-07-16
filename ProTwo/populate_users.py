import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'ProTwo.settings')

import django
django.setup()

from appTwo.models import User
from faker import Faker


fakegen = Faker()

def populate(N=5):
    for ent in range(N):
        fake_name = fakegen.name().split()
        fake_f_name = fake_name[0]
        fake_l_name = fake_name[1]
        fake_email = fakegen.email()


        user = User.objects.get_or_create(f_name=fake_f_name,
                                         l_name=fake_l_name,
                                         email=fake_email)[0]

if __name__=='__main__':
    print("POPULATING DATABASES")
    populate(20)
    print("COMPLETE!")
