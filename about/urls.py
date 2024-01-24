from about.views import Contributors
from django.urls import path

urlpatterns = [
    path('the-team', Contributors, name='meet-the-team'),
]
