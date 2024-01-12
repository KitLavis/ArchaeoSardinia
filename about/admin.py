from django.contrib import admin
from .models import Contributor
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contributor)
class ContributorAdmin(SummernoteModelAdmin):

    list_display = ('name', 'role', 'created_on')
    search_fields = ['name', 'role']
    summernote_fields = ('background', 'motivation')
