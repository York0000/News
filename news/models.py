from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from image_cropping import ImageRatioField

from authors.models import AuthorModel
from categories.models import CategoryModel


class NewsModel(models.Model):
    title = models.CharField(max_length=200)
    page_count = models.IntegerField(null=True, blank=True)

    cover = models.ImageField(upload_to='covers', null=True,)
    cropping = ImageRatioField('cover', '100x100', free_crop=True)

    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT,
                               related_name='news')
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT,
                                 related_name='news',
                                 null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    description = RichTextUploadingField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
