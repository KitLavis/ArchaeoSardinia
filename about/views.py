from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Contributor


def Contributors(request):

    queryset = Contributor.objects.order_by('name')

    return render (
        request,
        template_name="contributors.html",
        context={
            "contributors": queryset
        },
    )
