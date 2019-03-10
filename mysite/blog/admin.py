from django.contrib import admin
from .models import BlogArtcles

@admin.register(BlogArtcles)
class BlogArtclesAdmin(admin.ModelAdmin):
    list_display = ('title',  'author', 'publish')
    list_filter = ( 'publish', 'author')
    search_fields = ('title', 'body')  #搜索
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('-publish','author')

