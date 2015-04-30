from django.db import models

class Address(models.Model):
	address = models.CharField(max_length=50)
	postal_code = models.CharField(max_length=6)
	apartment_number = models.IntegerField(max_length=4)