from about.views import Contributors
from django.urls import path

urlpatterns = [
    # path('our-goal', views.OurGoals.as_view(), name='our-goals'),
    path('the-team', Contributors, name='meet-the-team'),
]