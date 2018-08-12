"""
Definition of urls for DjangoWebProject_gtts.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()
from django.conf.urls import include, url
import gtts.views

urlpatterns = [
    url(r'^$', gtts.views.index, name='index'),
    url(r'^home$', gtts.views.index, name='home'),
]
