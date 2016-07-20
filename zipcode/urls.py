from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MainView.as_view(), name='main'),
)
