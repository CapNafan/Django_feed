from django.contrib import admin
from .models import NewsItem


@admin.register(NewsItem)
class NewItemAdmin(admin.ModelAdmin):
    pass
