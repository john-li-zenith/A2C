from django.conf.urls import patterns, include, url
from apps.views import AppListView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns(
    '',
    url(r'^list/$', login_required(AppListView.as_view()), name='applist'),
    url(r'^upload/$','apps.views.app_upload',name='app-upload'),
    
    )
