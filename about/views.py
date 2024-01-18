from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Contributor


def Contributors(request):

    queryset = Contributor.objects.order_by('created_on')
    new_recruit = queryset.latest()

    return render (
        request,
        template_name="contributors.html",
        context={
            "contributors": queryset,
            "new_recruit": new_recruit
        },
    )
