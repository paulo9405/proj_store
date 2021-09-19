from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100, null=True)

    class Meta:
        unique_together = ('name',)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100, null=True)

    class Meta:
        unique_together = ('name',)

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=100, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('name', 'country')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('name', 'province')

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    latitude = models.FloatField(max_length=100, null=True)
    longitude = models.FloatField(max_length=100, null=True)
    postalCode = models.IntegerField(null=True)

    class Meta:
        unique_together = (
            'street', 'city', 'latitude', 'longitude', 'postalCode')

    def __str__(self):
        return self.street


class Store(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE,
                                   null=True)
    websites = models.CharField(max_length=100, null=True)

    class Meta:
        unique_together = ('name', 'address', 'categories', 'websites')

    def __str__(self):
        return self.name
