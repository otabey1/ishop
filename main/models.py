from django.db import models


class Review(models.Model):
    user = models.ForeignKey('client.User', on_delete=models.RESTRICT)
    comment = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0
    admin = models.ForeignKey('client.User', on_delete=models.RESTRICT, default=None, null=True)
    parent = models.ForeignKey('Category', on_delete=models.RESTRICT, null=True, default=None, blank=True)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    status = models.SmallIntegerField(choices=(
        (STATUS_ACTIVE, 'Faol'),
        (STATUS_INACTIVE, 'Nofaol')
    ), default=STATUS_ACTIVE)

    def __str__(self):

        return self.name_uz


class Unit(models.Model):
    name_uz = models.CharField(max_length=45)
    name_ru = models.CharField(max_length=45)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    availability_unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    content_uz = models.TextField()
    content_ru = models.CharField(max_length=45)
    anons_uz = models.CharField(max_length=50)
    anons_ru = models.CharField(max_length=45)
    price = models.BigIntegerField(primary_key=True)
    discount_percent = models.SmallIntegerField(blank=True)
    discount_start = models.DateTimeField(auto_now_add=True)
    discount_end = models.DateTimeField(auto_now_add=True)
    vendor_code = models.CharField(max_length=15)
    photo0 = models.ImageField()
    photo1 = models.ImageField()
    photo2 = models.ImageField()
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)


class ProductReview(models.Model):
    user = models.ForeignKey('client.User', on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)


class PromoCode(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    availability = models.IntegerField(default=0)
    used = models.IntegerField(default=0)
    discount = models.SmallIntegerField(default=10)


class Setting(models.Model):
    key = models.CharField(max_length=50)
    value = models.TextField()


class Post(models.Model):
    subject_uz = models.CharField(max_length=100)
    subject_ru = models.CharField(max_length=100)
    content_uz = models.TextField()
    content_ru = models.TextField()
    photo = models.ImageField()
    status = models.SmallIntegerField(primary_key=True)
    created_ad = models.DateTimeField(auto_now_add=True)


class PostComment(models.Model):
    parent = models.ForeignKey('PostComment', on_delete=models.RESTRICT, null=True, default=None, blank=True)
    post = models.ForeignKey(Post, on_delete=models.RESTRICT)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models .DateTimeField(auto_now=True)
