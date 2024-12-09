"""
URL configuration for PortfolioBase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PortfolioHome import views
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static for media file handling

urlpatterns = [
    path('', views.Home, name='home'),
    
    path('projects', views.Projects, name='projects'),
    path('admin/', admin.site.urls),
    path('platforms/', views.platforms_view, name='platforms'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:  # Ensure it's only active in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)