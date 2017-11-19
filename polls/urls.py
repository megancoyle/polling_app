from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^polls/$', views.PollsView.as_view(), name='polls'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
