from django.conf.urls import include, url
from django.contrib import admin
from . import views 

urlpatterns = [
    url(r'^listing/id/(?P<listing_id>\d+)/$', views.listing, name='listing'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', views.home, name='home')
]
