from django.db import models
from address import Address
from django.contrib.auth.models import User


# TODO: Start and end date

class House(models.Model):
	address = models.OneToOneField(Address, null=True)
	rent_per_month = models.IntegerField(default=0)
	number_of_rooms = models.IntegerField(default=1)
	number_of_bathrooms = models.IntegerField(default=1)

	# optional
	average_cost_utilities = models.IntegerField(default=0)
	number_of_roommates = models.IntegerField(default=0)


class Posting(models.Model):
	title = models.CharField(max_length=150)
	description = models.CharField(max_length=500)
	number_of_semesters = models.IntegerField(default=0)
	house = models.OneToOneField(House, null=True)
	user_profile = models.ForeignKey(User, related_name="profile", null=True)


class Image(models.Model):
	photo = models.ImageField(upload_to="photos/")
	posting = models.ForeignKey(Posting, related_name="images")
