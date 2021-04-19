from django.contrib import admin

from authors.models import AuthorModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    search_fields = ['name']
