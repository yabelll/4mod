from django.urls import path
from .views import index, top_sellers, advertisements_post, advertisements_detail

urlpatterns = [
    path('', index, name='main-page'),
    path('top_sellers/', top_sellers, name='top_sellers'),
    path('advertisement-post/', advertisements_post, name='adv-post'),
    path('advertisement/<int:pk>', advertisements_detail, name= 'adv-detail')
]