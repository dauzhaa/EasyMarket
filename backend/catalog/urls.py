from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'catalog'

router = DefaultRouter()

router.register(r'', views.ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls))
]
    