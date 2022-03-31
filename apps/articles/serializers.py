from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers

from apps.articles.models import Article
from apps.categories.models import Category
from apps.tags.models import Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "slug",
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "id",
            "name",
            "slug",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        )


class ArticleSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    category = CategorySerializer()
    tag = TagSerializer(many=True)
    author = UserSerializer()

    class Meta:
        model = Article
        fields = (
            "id",
            "name",
            "slug",
            "image",
            "category",
            "tag",
            "author",
        )
        depth = 1

    def get_image(self, obj):
        return f"{settings.BASE_URL}/media/{obj.image}"


class ArticleDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    category = CategorySerializer()
    tag = TagSerializer(many=True)
    author = UserSerializer()

    class Meta:
        model = Article
        fields = (
            "id",
            "name",
            "slug",
            "content",
            "image",
            "category",
            "tag",
            "author",
        )
        depth = 1

    def get_image(self, obj):
        return f"{settings.BASE_URL}/media/{obj.image}"