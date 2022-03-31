import os
import time
from django.contrib.auth.models import User
from django.db import models
from apps.core.models import TimeStampedAbstractModel
from tinymce.models import HTMLField
from apps.categories.models import Category
from apps.tags.models import Tag


def post_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / uploads/ posts/ post_time
    upload_to = 'uploads/article/'
    ext = filename.split('.')[-1]
    filename = 'post_{}.{}'.format(int(time.time()), ext)
    return os.path.join(upload_to, filename)


class Article(TimeStampedAbstractModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    content = HTMLField()
    image = models.ImageField(verbose_name="Image", upload_to=post_directory_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.name
