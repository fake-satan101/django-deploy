import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first.settings')
import django
django.setup()

from faker import Faker
from first_app.models import Sign_up

fake=Faker()
def Fake(a=11):

    for x in range(a):
        Name=fake.name()
        Email=fake.email()
        Password=fake.name()
        new=Sign_up.objects.get_or_create(name=Name,email=Email,password=Password)[0]
        new.save()
if __name__ =="__main__":

    b=input("Enter the number of records to populate the database:")
    if b!="":
        if type(int(b))==int:
            print("populating script!")
            Fake(int(b))
            print("populating complete!")
        else:
            print("invalid input, automatically populating 10 records")
            Fake()
            print("populating complete!")
    else:
        print("Nothing entered, automatically populating 10 records")
        Fake()
        print("populating complete!")
