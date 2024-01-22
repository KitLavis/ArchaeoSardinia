from django.contrib import admin
from .models import Contributor
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contributor)
class ContributorAdmin(SummernoteModelAdmin):
    """
    Lists the fields to be displayed in admin, prepopulates
    the slug, adds search functionality, add rich text
    to background and motivations fields
    """
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'role', 'created_on')
    search_fields = ['name', 'role']
    summernote_fields = ('background', 'motivation')
