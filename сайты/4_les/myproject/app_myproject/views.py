from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Advertisements, User
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count

def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisements.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisements.objects.all()
    context = {"advertisements": advertisements, 'title': title}
    return render(request, 'app_advertisements/index.html', context)

def top_sellers(request):
    users = User.objects.annotate(adv_count=Count('advertisements')).order_by('-adv_count')
    context = {'users': users}
    return render(request, 'app_advertisements/top-sellers.html', context)

@login_required(login_url=reverse_lazy('login'))
def advertisements_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisements = Advertisements(**form.cleaned_data)
            advertisements.user = request.user
            advertisements.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)

def advertisements_detail(request, pk):
    advertisement = Advertisements.objects.get(id=pk)
    context = {'adv': advertisement}
    return render(request, 'app_advertisements/advertisement.html', context)