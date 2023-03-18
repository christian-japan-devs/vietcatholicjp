from django.urls import path
from django.contrib.auth import views
from .views import (RegistrationListViewSet
)

urlpatterns = [
    path('api/event/youthday/get-ticket', RegistrationListViewSet.as_view({
        'get': 'getall',
    })),
    path('api/event/youthday/add-ticket', RegistrationListViewSet.as_view({
        'get': 'create',
    })),
]