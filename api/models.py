from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Address(models.Model):
    name = models.CharField(max_length=100)
    # 都道府県
    prefecture = models.CharField(max_length=100)
    # 市区町村
    city = models.CharField(max_length=100)
    # 町名
    town = models.CharField(max_length=100)
    # 番地
    street = models.CharField(max_length=100)
    # 建物名
    building = models.CharField(max_length=100)

    def __str__(self):
        return self.name
