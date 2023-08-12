from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Room(models.Model):
    class BedChoice(models.TextChoices):
        ONE = "One bed"
        TWO = "Two bed"

    image = models.ImageField(upload_to="room/")
    star = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=155)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    person = models.PositiveIntegerField(default=1)
    bed_choice = models.CharField(max_length=50, choices=BedChoice.choices,
                                  default=BedChoice.ONE)
    wifi = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)
    condition = models.BooleanField(default=False)
    sqm = models.FloatField(default=12)
    dostovka = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    elevators = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Blog(models.Model):
    image = models.ImageField(upload_to="blog/")
    title = models.CharField(max_length=155)
    description = models.TextField()
    create_at = models.DateTimeField(auto_created=True)
    author = models.ForeignKey(to="app.User",
                               on_delete=models.CASCADE,
                               related_name="blogs")


class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    subject = models.CharField(max_length=155)
    text = models.TextField()

    def __str__(self):
        return self.email


class HotelStaff(models.Model):

    image = models.ImageField(upload_to="staff/")
    name = models.CharField(max_length=155)
    position = models.CharField(max_length=155)
    company = models.CharField(max_length=155)
    experience = models.CharField(max_length=155)
    email = models.EmailField()
    phone_number = models.CharField(max_length=155)
    language_skill1 = models.CharField(max_length=155, null=True, blank=True)
    language_skill2 = models.CharField(max_length=155, null=True, blank=True)
    language_skill3 = models.CharField(max_length=155, null=True, blank=True)
    language_skill4 = models.CharField(max_length=155, null=True, blank=True)


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Users must have a phone number!')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=155, unique=False)

    email = models.EmailField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(('phone number'), validators=[phone_regex], max_length=17, unique=True)  #

    address = models.CharField(max_length=155, null=True, blank=True)
    # forget_password_token = models.CharField(max_length=100)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()
