from django.db import models
from apps.core.models import TimeStampedAbstractModel


class Category(TimeStampedAbstractModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
