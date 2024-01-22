from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
   """
    Lists the fields to be displayed in admin, prepopulates
    the slug, adds search functionality, add rich text
    to content field
    """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Lists the fields to be displayed in admin, adds search
    functionality, adds filtering functionality
    """
    list_display = ('name', 'content', 'post', 'created_on')
    list_filter = ('created_on', 'name')
    search_fields = ['name', 'content']
