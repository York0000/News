from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from news.models import NewsModel


class NewsModelForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = NewsModel
        exclude = ['created_at', 'updated_at']
