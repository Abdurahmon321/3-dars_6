from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=255, verbose_name="kategoriya")

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriayalar"


class Color(models.Model):
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = "Rang"
        verbose_name_plural = "Ranglar"


class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
    image = models.ImageField(upload_to='static/car_images/')
    name = models.CharField(max_length=255, verbose_name="Mashina nomi")
    price = models.IntegerField(verbose_name="narxi")
    color = models.ForeignKey(Color,on_delete=models.CASCADE, verbose_name="rangi")
    max_speed = models.IntegerField(verbose_name="maxsimal tezligi")
    quantity = models.IntegerField(verbose_name="Soni")
    discription = models.TextField(blank=True, null=True, verbose_name="tarif")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mashina"
        verbose_name_plural = "Mashinalar"


class Customer(models.Model):
    firstname = models.CharField(max_length=255, verbose_name="ismi")
    lastname = models.CharField(max_length=255, verbose_name="familyasi")
    phone_number = models.CharField(max_length=255, verbose_name="telefon raqami")
    email = models.CharField(max_length=255, verbose_name="elektron pochtasi")
    address = models.CharField(max_length=255, verbose_name="Manzili")

    def __str__(self):
        return self.firstname

    class Meta:
        verbose_name = "Xaridor"
        verbose_name_plural = "Xaridorlar"


class Employee(models.Model):
    name = models.CharField(max_length=255, verbose_name="ismi")
    phone_number = models.CharField(max_length=255, verbose_name="telefon raqami")
    email = models.CharField(max_length=255, verbose_name="elektron pochtasi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ishchi"
        verbose_name_plural = "Ishchilar"
