from django.conf.urls import include, url
from rest_framework import routers
from django.contrib import admin
from marketplace import views

router = routers.DefaultRouter()
router.register(r'listing', views.ListingViewSet)
#router.register(r'listingid/(?P<listing_id>[0-9]+)/$', views.ListingViewSet)
router.register(r'merchant', views.MerchantViewSet)
router.register(r'message', views.MessageViewSet)
router.register(r'transaction', views.TransactionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^create_user/', views.create_user, name ='create_user'),
    url(r'^verify_user/', views.verify_user, name = 'verify_user')
]
