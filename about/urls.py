from about.views import TeamList
from django.urls import path

urlpatterns = [
    # path('our-goal', views.OurGoals.as_view(), name='our-goals'),
    path('the-team', TeamList.as_view(), name='meet-the-team'),
]