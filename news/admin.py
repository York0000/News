from django.contrib import admin
from image_cropping import ImageCroppingMixin

from news.models import NewsModel


@admin.register(NewsModel)
class NewsModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    search_fields = ['title', 'author']
    list_display = ['title', 'author', 'page_count', 'created_at']
    list_filter = ['created_at']
