"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings 
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from drf import views

router = routers.DefaultRouter()
router.register(
    r'api', views.AllProductsViewSet, basename="all products")
router.register(
    r'users', views.UserViewSet, basename="all users")
router.register(
    r'comments', views.CommentsViewSet, basename="all comments")
router.register(
    r'profile', views.ProfileViewSet, basename="all cprofiles")
router.register(
    r'order', views.OrderViewSet, basename="all orders")
router.register(
    r'orderproduct', views.OrderProductViewSet, basename="all orders with products and quant")
router.register(
    r'rentproduct', views.RentProductViewSet, basename="rent order history")
router.register(
    r'rentready', views.RentReadyProducts, basename="tylko dostepne")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path("", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)