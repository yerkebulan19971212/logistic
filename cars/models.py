from django.db import models


class Driver(models.Model):
    GENDER_CHOICE = [
        ('Male', 'мужской'),
        ('Female', 'женский'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICE)

    def __str__(self):
        return " ".join([self.first_name, self.last_name])


class Car(models.Model):
    photo = models.ImageField(upload_to='cars/')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    mark = models.CharField(max_length=512)
    color = models.CharField(max_length=255)
    number = models.CharField(max_length=32, default="NONE")

    def __str__(self):
        return " ".join([self.driver.first_name, self.mark])


class Order(models.Model):
    TypeFileds = [
        (0, 'Такси'),
        (1, 'Доставка'),
    ]
    type = models.IntegerField(choices=TypeFileds, default=0)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    fromm = models.CharField(max_length=255, default='')
    to = models.CharField(max_length=255, default='')
    time = models.DateTimeField(null=True)
    email = models.EmailField(null=True)
    order_time = models.DateTimeField()
    datetime = models.DateTimeField(auto_now=True)


class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
