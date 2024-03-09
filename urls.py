from django.contrib import admin
from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

