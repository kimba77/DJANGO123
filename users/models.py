from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    GENDER_TYPE = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
    OCCUPATION_CHOICE = (
        ("Student", "Student"),
        ("Worker", "Worker"),
        ("Jobless", "Jobless"),
        ("Retired", "Retired"),
    )
    gender = models.CharField(choices=GENDER_TYPE, max_length=100)
    phone_number = models.CharField(max_length=100)
    code_word = models.CharField(max_length=255)
    occupation = models.CharField(choices=OCCUPATION_CHOICE, max_length=100)
    age = models.DateField(null=True)
