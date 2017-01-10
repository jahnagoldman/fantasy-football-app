from django.conf.urls import url

from team.views import TeamPage
from . import views

urlpatterns = [url(r'^', TeamPage.as_view(), name='team-list'),

               ]
