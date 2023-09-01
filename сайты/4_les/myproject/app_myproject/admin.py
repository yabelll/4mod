from django.contrib import admin
from .models import Advertisements
from django.utils.safestring import mark_safe

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "created_date", "updated_date", "auction", "imagepr"]
    list_filter = ["auction", "created_at"]
    readonly_fields = ['imagepr']
    actions = ["make_auction_as_False", "make_auction_as_True"]
    fieldsets = (
                ("Общее", {
                    "fields": ("title", "description", "image", 'imagepr')
                    }), 
                ("Финансы", {
                    "fields": ("price", "auction"),
                    "classes": ["collapse"]
                    })
    )

    def imagepr(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')

    @admin.action(description="Убрать возможность торга")
    def make_auction_as_False(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_True(self, request, queryset):
        queryset.update(auction = True)

admin.site.register(Advertisements, AdvertisementAdmin)