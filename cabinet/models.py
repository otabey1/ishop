from django.db import models

# Create your models here.


class Category(models.Model):
    # user = models.ForeignKey(User, on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)


class Unit(models.Model):
    name_uz = models.CharField(max_length=45)
    name_ru = models.CharField(max_length=45)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    availability_unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    content_uz = models.CharField(max_length=45)
    content_ru = models.CharField(max_length=45)
    anons_uz = models.CharField(max_length=50)
    anons_ru = models.CharField(max_length=45)
    price = models.BigIntegerField(primary_key=True)
    discount_percent = models.SmallIntegerField(blank=True)
    discount_start = models.DateTimeField()
    discount_end = models.DateTimeField()
    vendor_code = models.CharField(max_length=15)
    photo0 = models.ImageField(max_length=255)
    photo1 = models.ImageField(max_length=255)
    photo2 = models.ImageField(max_length=255)
    created_ad = models.DateTimeField()
    updated_ad = models.DateTimeField()


class Post(models.Model):
    subject_uz = models.CharField(max_length=100)
    subject_ru = models.CharField(max_length=100)
    content_uz = models.TextField(blank=True)
    content_ru = models.TextField(blank=True)
    photo = models.ImageField(max_length=255)
    status = models.SmallIntegerField(primary_key=True)
    created_ad = models.DateTimeField()


class PostComment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.RESTRICT)
    comment = models.TextField(blank=True)


class Review(models.Model):
    # user = models.ForeignKey(User, on_delete=models.RESTRICT)
    comment = models.TextField(blank=True)
    created_ad = models.DateTimeField()
