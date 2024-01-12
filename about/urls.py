from . import views
from django.urls import path

urlpatterns = [
    path('our-goal', views.OurGoals.as_view(), name='our-goals'),
    path('contributors', views.Contirbutors.as_view(), name='the-contributors'),
]