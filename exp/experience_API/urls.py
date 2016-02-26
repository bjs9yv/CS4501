from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^listing_service/', views.listing_service, name='listing_service'),
    url(r'^admin/', include(admin.site.urls)),
]
