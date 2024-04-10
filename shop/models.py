from django.conf import settings
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    model = models.CharField(verbose_name='Модель', max_length=70)
    data = models.DateField(verbose_name='Дата_выхода')


class Factory(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название завода')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Контакты', on_delete=models.CASCADE)


class Retail(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название ритейла')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Контакты', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)

    def sum(self):
        return self.quantity*self.product.price


class Entrepreneur(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название_ИП')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Контакты', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, blank=True, null=True)
    retail = models.ForeignKey(Retail, on_delete=models.CASCADE, blank=True, null=True)

    def sum(self):
        return self.quantity*self.product.price
