from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Booker(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True)
    address = models.CharField( max_length=250, null=True)
    phone = models.IntegerField(default=0000000000)


    def __str__(self):
        return self.user.username

class Train(models.Model):

    train_name = models.CharField(max_length=100)
    train_number = models.CharField(max_length=225)
    rows_available = models.IntegerField()
    available_seats = models.CharField( max_length=225,null=True)
    window_seats = models.CharField(max_length=225,null=True)
    seat_agent = models.CharField(max_length=225,null=True)
    booked_seats = models.CharField(max_length=225,null=True)
    middle_seats = models.CharField( max_length=250, null=True)
    aisle_seats = models.CharField( max_length=250, null=True)

    def __str__(self):
        return self.train_name

class Passengers(models.Model):
    booker = models.ForeignKey(Booker, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=100)
    age = models.IntegerField()

    gender_choices=[('Male', 'Male'),
    ('Female', 'Female'),]
    gender = models.CharField(max_length=50, choices=gender_choices)

    seat_number = models.IntegerField()

    def __str__(self):
        return self.p_name



