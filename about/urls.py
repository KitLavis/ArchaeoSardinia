from . import views
from django.urls import path

urlpatterns = [
    # path('our-goal', views.OurGoals.as_view(), name='our-goals'),
    path('the-team', views.TeamList.as_view(), name='meet-the-team'),
]