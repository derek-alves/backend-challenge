from django.urls import path, include
from .views import PlaceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('place', PlaceViewSet, basename='place')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', include(router.urls)),
]
