from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'entries', EntryViewSet)
router.register(r'exits', ExitViewSet)
router.register(r'stores', StoreViewSet)

urlpatterns = [
     
     
     # Url patterns for django rest framework
     path('api-auth/', include('rest_framework.urls')),
     path('api/', include(router.urls)),
     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]