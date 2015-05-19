from django import forms
from .models import Posting, House, Image
from address import Address
from django.forms.models import inlineformset_factory


class PostDescription(forms.ModelForm):
	title = forms.CharField(max_length=128)
	description = forms.CharField(max_length=500, widget=forms.Textarea)
	number_of_semesters = forms.ChoiceField(choices=[(x, x) for x in range(0, 6)])

	class Meta:
		model = Posting
		fields = ('title', 'description', 'number_of_semesters',)
		exclude = ('house', 'images', 'user_profile')
		widgets = {
		'title' : forms.TextInput(attrs={'class': 'input-field'})
		}


class HouseDescription(forms.ModelForm):
	rent_per_month = forms.ChoiceField(choices=[(x, x) for x in range(10, 1000, 10)])
	number_of_roommates = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)])
	number_of_rooms = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)])
	number_of_bathrooms = forms.ChoiceField(choices=[(x, x) for x in range(0, 5)])
	average_cost_utilities = forms.ChoiceField(choices=[(x, x) for x in range(0, 200, 5)])

	class Meta:
		model = House
		fields = ('rent_per_month', 'number_of_rooms', 'number_of_bathrooms',
				  'average_cost_utilities', 'number_of_roommates')
		exclude = ('address',)


class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = ('address', 'postal_code')


PictureFormSet = inlineformset_factory(Posting, Image, extra=6, can_delete=False, exclude=())
