from __future__ import unicode_literals

from custom_user.models import CustomUser
from django.db import models


class MotorMake(models.Model):
    brand = models.CharField(max_length=120)

    @property
    def models(self):
        instance = self
        qs = MotorModel.objects.filter_by_instance(instance)
        return qs

    def __unicode__(self):
        return str(self.brand)


class MotorModel(models.Model):
    make = models.ForeignKey(MotorMake)
    model = models.CharField(max_length=120)

    def __unicode__(self):
        return str(self.model)


class MotorStyle(models.Model):
    style = models.CharField(max_length=120)

    def __unicode__(self):
        return str(self.style)


class MotorEngine(models.Model):
    cc = models.CharField(max_length=120)

    def __unicode__(self):
        return str(self.cc)


class Motorcycle(models.Model):
    make = models.ForeignKey(MotorMake)
    model = models.ForeignKey(MotorModel)
    style = models.ForeignKey(MotorStyle)
    engine_size = models.ForeignKey(MotorEngine)
    production_year = models.CharField(max_length=10)
    color = models.CharField(max_length=120)
    default = models.BooleanField(default=False)

class BicycleMake(models.Model):
    brand = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.brand)


class BicyceStyle(models.Model):
    style = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.style)


class Bicycle(models.Model):
    make = models.ForeignKey(BicycleMake)
    style = models.ForeignKey(BicyceStyle)
    color = models.CharField(max_length=120)
    default = models.BooleanField(default=False)

class Garage(models.Model):
    user = models.OneToOneField(CustomUser)
    bicycles = models.ManyToManyField(Bicycle, blank=True)
    motorcycles = models.ManyToManyField(Motorcycle, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.user.email) + " " + "Garage"

class NewBicycle(models.Model):
    make = models.CharField(max_length=120)
    style = models.CharField(max_length=120)

    def __unicode__(self):
        return str(self.make) + '---' + str(self.style)

class NewMotorcycle(models.Model):
    make = models.CharField(max_length=120)
    style = models.CharField(max_length=120)
    engine_size = models.CharField(max_length=120)
    model = models.CharField(max_length=120)

    def __unicode__(self):
        return str(self.make) + '---' + str(self.style)



