from django.contrib import admin

from apps.tags.models import Tag


class TagAdmin(admin.ModelAdmin):
    model = Tag
    prepopulated_fields = {'slug': ('name',)}

    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name', 'slug')
    ordering = ('-created_at',)

    fieldsets = (
        ('Tag Info', {'fields': ('name', 'slug')}),
        ('Other info', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at',)


admin.site.register(Tag, TagAdmin)
