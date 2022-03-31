from django.db import models
from apps.core.models import TimeStampedAbstractModel


class Tag(TimeStampedAbstractModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        db_table = 'tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name
