from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.quotes.views import QuoteWall

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', QuoteWall.as_view(), name='wall'),
    url(r'^admin/', include(admin.site.urls)),
)
