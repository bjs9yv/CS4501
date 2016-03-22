from django.conf.urls import include, url
from django.contrib import admin
from . import views 

urlpatterns = [
    url(r'^listing/id/(?P<listing_id>\d+)/$', views.listing, name='listing'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create_account/', views.create_account, name='create_account'),
    url(r'^create_listing/', views.create_listing, name='create_listing'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^', views.home, name='home')
]
