from django.contrib import admin
from .models import main
@admin.register(main)
class mainAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'visits', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
