from django.db import models


class Driver(models.Model):
    GENDER_CHOICE = [
        ('Male', 'мужской'),
        ('Female', 'женский'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=7,  choices=GENDER_CHOICE)


class Car(models.Model):
    photo = models.ImageField(upload_to='cars/')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    mark = models.CharField(max_length=512)
    color = models.CharField(max_length=255)
    number = models.CharField(max_length=32, default="NONE")


class Order(models.Model):
    TypeFileds = [
        (0, 'Такси'),
        (1, 'доставка'),
    ]
    type = models.IntegerField(choices=TypeFileds, default=0)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    _from = models.CharField(max_length=255, default='')
    to = models.CharField(max_length=255, default='')
    time = models.DateTimeField()
    order_time = models.DateTimeField()
    datetime = models.DateTimeField(auto_created=True)


