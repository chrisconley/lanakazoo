import django.contrib.auth.models as auth_models
from django.db import models

# Compatibile with Mysql and sqlite
class BlobField(models.Field):
    description = "Blob"
    def db_type(self, connection):
        return 'blob'

class Purchase(models.Model):
    name = models.CharField(max_length=100)
    store = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    #image = models.ForeignKey('Image')
    portion_name = models.CharField(max_length=50)
    portion_amount = models.FloatField()
    notes = models.TextField()

class Meal(models.Model):
    user = models.ForeignKey(auth_models.User)
    name = models.CharField(max_length=100)
    people = models.IntegerField()
    #- total_cost (read only custom method)
    #- cost_per_person (read only)
    #- cost_per_person_per_month (read only)
    #- has_many: consumables

class Consumable(models.Model):
    purchase = models.ForeignKey('Purchase', related_name='consumables')
    portions = models.IntegerField()

class Image(models.Model):
    name = models.CharField(max_length=100)
    data = BlobField()
