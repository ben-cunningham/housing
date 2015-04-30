from django.shortcuts import render, redirect
from .models import Posting, House
from .forms import PostDescription, HouseDescription, AddressForm, PictureFormSet
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


def get_uid(request):
	if request.user.is_authenticated():
		social = request.user.social_auth.get(provider='facebook')
		return {"user_id": social.uid}
	else:
		return {}


def landing_view(request):
	return render(request, 'co_op/landing_view.html')


def list_view(request):
	postings = zip_postings(Posting.objects.all())
	print(postings)
	return render(request, 'co_op/list_view.html', {'postings': postings})


def zip_postings(postings):
	postings = list(postings)
	postings.append(None)
	even = len(postings) % 2 == 0
	zipped = zip(*[iter(postings)] * 2)

	return zipped


def form_view(request):
	if request.method == "POST":

		post_form = PostDescription(request.POST, prefix='fm')
		house_form = HouseDescription(request.POST, prefix='hs')
		address_form = AddressForm(request.POST, prefix='ads')

		if post_form.is_valid() and house_form.is_valid() and address_form.is_valid():
			post = post_form.save(commit=True)
			post.house = house_form.save()
			post.house.address = address_form.save()

			image_formset = PictureFormSet(request.POST, request.FILES, instance=post)
			if image_formset.is_valid():
				post.user_profile = request.user
				post.save()
				image_formset.save()
				return redirect('co_op.views.list_view')

		return redirect('co_op.views.list_view')

	else:
		post_form = PostDescription(prefix='fm')
		house_form = HouseDescription(prefix='hs')
		picture_formset = PictureFormSet(instance=Posting())
		address_form = AddressForm(prefix='ads')

		return render(request, 'co_op/form_view.html', {'descForm': post_form,
														'houseForm': house_form,
														'picForm': picture_formset,
														'addressForm': address_form
														})


def detail_view(request, post_id):
	housePosting = Posting.objects.get(pk=post_id)
	ImageSet = housePosting.images.all()
	firstImage = ImageSet[0].photo
	# print(housePosting.user.first_name)

	return render(request, 'co_op/detail_view.html', {'posting': housePosting,
													  'images': ImageSet,
													  'first_image': firstImage})


def user_postings(request):
	postings = Posting.objects.filter(user_profile=request.user)
	postings = zip_postings(postings)
	return render(request, 'co_op/list_view.html', {'postings': postings })

def logout(request):
	auth_logout(request)
	return redirect('/')

