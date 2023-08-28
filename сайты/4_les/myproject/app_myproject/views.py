from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisements
from .forms import AdvertisementForm

def index(request):
    advertisements = Advertisements.objects.all()
    context = {"advertisements": advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisements_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisements = Advertisements(**form.cleaned_data)
            form.user = request.user
            form.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    return render(request, 'advertisement-post.html', {'form': form})