"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import ( 
CompanyViewSet, DepartmentViewSet, CompanyDepartmentViewSet,
UserViewSet, TicketViewSet, CommentViewSet, NotificationLogViewSet
)
from rest_framework_simplejwt.views import (
TokenObtainPairView, TokenRefreshView,
)
from .views.registration import RegisterView

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'company-departments', CompanyDepartmentViewSet)
router.register(r'users', UserViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'notifications', NotificationLogViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name= 'token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name="register'),
]
