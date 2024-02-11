from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Links (models.Model):
    short = models.SlugField('Short link', unique=True)
    long = models.CharField('Long link', max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        return self.short

    def get_absolute_url(self):
        return reverse('links')