from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'entries', EntryViewSet)
router.register(r'exits', ExitViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
     path('stores/<str:store>/', actual_view),
     path('stores/<str:store>/stats/', stats_view),
     #path('api-auth/', include('rest_framework.urls')),
     path('api/', include(router.urls)),
     path('api-token-auth/', obtain_auth_token, name='login'),
     
     path('api/total_entries_by_day/', total_entries_by_day, name='total_entries_by_day'),
     path('api/total_entries_by_month/', total_entries_by_month, name='total_entries_by_month'),
     path('api/total_entries_last_week/', total_entries_last_week, name='total_entries_last_week'),
]