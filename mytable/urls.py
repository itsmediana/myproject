from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyTableViewSet

router = DefaultRouter()
router.register(r'mytable', MyTableViewSet)  # Подключаем API

urlpatterns = [
    path('', include(router.urls)),  # Включаем маршруты API
]
