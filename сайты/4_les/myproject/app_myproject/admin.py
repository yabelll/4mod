from django.contrib import admin
from .models import Advertisements

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "created_at", "auction"]
    list_filter = ["auction", "created_at"]
    actions = ["make_auction_as_False", "make_auction_as_True"]


    @admin.action(description="Убрать возможность торга")
    def make_auction_as_False(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_True(self, request, queryset):
        queryset.update(auction = True)

admin.site.register(Advertisements, AdvertisementAdmin)

# Register your models here.
