from django.contrib import admin
from django.urls import path, include
# from auth import urls as auth_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('auth.urls')),
]
