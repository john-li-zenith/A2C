from django.conf.urls import patterns, include, url
from apps.views import AppListView,AppLogListView, AppUpdateCreateView,AppUploadCreateView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns(
    '',
    url(r'^list/$', login_required(AppListView.as_view()), name='applist'),
    url(r'^log/(\d+)/$', login_required(AppLogListView.as_view()), name='applog'),
    url(r'^upload/$',login_required(AppUploadCreateView.as_view()),name='app-upload'),
    url(r'^update/$',login_required(AppUpdateCreateView.as_view()),name='app-update'),
    
    )
