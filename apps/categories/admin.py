from django.contrib import admin

from apps.categories.models import Category


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug': ('name',)}

    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name', 'slug')
    ordering = ('-created_at',)

    fieldsets = (
        ('Category Info', {'fields': ('name', 'slug')}),
        ('Other info', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at',)


admin.site.register(Category, CategoryAdmin)
