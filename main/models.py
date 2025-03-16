from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True)
    description = models.TextField(max_length=255, unique=True)
    image = models.ImageField(upload_to='services/')
    image_link = models.CharField(max_length=255, default='')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_services'
        ordering = ('sort', 'name')
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True)
    small_desc = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=255, unique=True)
    image = models.ImageField(upload_to='portfolios/')
    client = models.CharField(max_length=50) #Можна було розширити в окремий клас, але цього не робив для спрощення
    category = models.CharField(max_length=50) #Можна було розширити в окремий клас, але цього не робив для спрощення

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_portfolios'
        ordering = ('sort', 'name')
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

    def __str__(self):
        return self.name

class History(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True)
    description = models.TextField(max_length=255, unique=True)
    date = models.CharField(max_length=50)
    image = models.ImageField(upload_to='history/')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_history'
        ordering = ('sort', 'name')
        verbose_name = 'History'
        verbose_name_plural = 'Histories'

    def __str__(self):
        return self.name

class Staff(models.Model):
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True)
    role = models.CharField(max_length=50)
    image = models.ImageField(upload_to='staff/')
    twitter_link = models.URLField(max_length=225)
    facebook_link = models.URLField(max_length=225)
    linkedin_link = models.URLField(max_length=225)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_staff'
        ordering = ('sort', 'first_name', 'last_name')
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Partner(models.Model):
    name = models.CharField(max_length=50, unique=True)
    link = models.URLField(max_length=225)
    image = models.ImageField(upload_to='partner/')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_partner'
        ordering = ('sort', 'name')
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

    def __str__(self):
        return self.name

class Contact(models.Model):
    twitter_link = models.URLField(max_length=225)
    facebook_link = models.URLField(max_length=225)
    linkedin_link = models.URLField(max_length=225)

    class Meta:
        db_table = 'main_contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class UserMessage(models.Model):
    phone_regex = RegexValidator(r'^\+?(38)?\d{10}$')

    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50, validators=[phone_regex])
    message = models.TextField(max_length=255)

    is_confirmed = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'main_user_messages'
        ordering = ('-date_created',)