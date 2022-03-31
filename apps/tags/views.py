from rest_framework import generics

from apps.tags.serializers import TagSerializer
from apps.tags.models import Tag


class TagView(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = None
