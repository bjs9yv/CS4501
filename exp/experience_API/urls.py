from django.conf.urls import include, url
from django.contrib import admin
from experience_API import views

urlpatterns = [
    url(r'^listing_service/', views.listing_service, name='listing_service'),
    url(r'^recent_listings/', views.recent_listings, name='recent_listings'),
    url(r'^login/', views.login, name='login'),
    url(r'^create_user/', views.create_user, name='create_user'),
    url(r'^admin/', include(admin.site.urls)),
]
