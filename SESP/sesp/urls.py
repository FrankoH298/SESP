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
     path('<str:store>', actual_view),
     path('<str:store>/stats', stats_view),

     path('api/', include(router.urls)),
     path('login/', obtain_auth_token, name='login'),
]