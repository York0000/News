from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'
