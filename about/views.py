from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Contributor


class TeamList(generic.ListView):

    models = Contributor
    queryset = Contributor.objects.order_by('name')
    template_name = 'contributors.html'
