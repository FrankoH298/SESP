from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'entries', EntryViewSet)
router.register(r'exits', ExitViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    
    path('api/total_entries_per_day/<int:pk>', total_entries_per_day, name='total_entries_per_day'),
    path('api/total_entries_per_month/<int:pk>', total_entries_per_month, name='total_entries_per_month'),
    path('api/total_entries_last_week/<int:pk>', total_entries_last_week, name='total_entries_last_week'),
    path('api/total_entries_per_hour_last_two_weeks/<int:pk>', total_entries_per_hour_last_two_weeks, name='total_entries_per_hour'),
]

react_routes = getattr(settings, 'REACT_ROUTES', [])

for route in react_routes:
    print(route)
    urlpatterns += [
        path('{}'.format(route), TemplateView.as_view(template_name='index.html'))
    ]
