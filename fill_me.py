'''
Name: fill_me
Description:
This script is used to auto-populate the django models. Member names are automatically
generated using faker module.

genEquipment: Accepts the ID "N" as an integer value and type to generate equipment
gen_fake_data: Generates members. Accepts N as the number to generate the number
of members.

Usage:
Simply run fill_me and it will autopopulate.


'''

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SocialClubLoaner.settings')


import django
django.setup()


import random
from faker import Faker
from loaner_app.models import Members,Equipment

fakeme = Faker()
status_list = ['Good', 'Not Renewed']
counter = 99

def genEquipment(N, type):

    eq_name = type + "#" + str(N)
    eq_type = type
    eqgen = Equipment.objects.get_or_create(name=eq_name, type=eq_type)




def gen_fake_data(N=5):
    for fake in range(N):
        status = random.choice(status_list)
        name = fakeme.name()
        names = name.split(" ")
        firstname = names[0]
        lastname = names[1]
        id = counter+N



        memgen = Members.objects.get_or_create(first_name=firstname, last_name=lastname, member_status=status)




if __name__ =='__main__':
    print("Populating model")

    gen_fake_data()
    genEquipment(5, "Chess Board")
    genEquipment(1, "Chess Clock")
    genEquipment(2, "Chess Board")
    genEquipment(6, "Chess Clock")
    genEquipment(2, "Chess Board")
    genEquipment(123, "Chess Clock")
    print("Finished")