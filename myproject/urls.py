from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('api/', include('mytable.urls')),  # Подключение API
]
