from django.contrib import admin

from apps.articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    prepopulated_fields = {'slug': ('name',)}

    list_display = ('name', 'slug', 'category', 'author', 'created_at',)
    search_fields = ('name', 'slug')
    ordering = ('-created_at',)

    fieldsets = (
        ('Article Info', {'fields': ('name', 'slug', 'content', 'image', 'category', 'tag')}),
        ('Other info', {'fields': ('author', 'created_at', 'updated_at')}),
    )
    readonly_fields = ('author', 'created_at', 'updated_at',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Article, ArticleAdmin)
