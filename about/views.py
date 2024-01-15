from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Contributor


class TeamList(generic.ListView):

    models = Contributor
    queryset = Contributor.objects.order_by('name')
    template_name = 'contributors.html'


class ContributorDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Contributor.objects
        contributor = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "contributor_detail.html",
            {
                "contributor": contributor
            },
        )
