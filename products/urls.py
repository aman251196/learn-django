from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

app_name="products"

router = DefaultRouter(trailing_slash=False)

router.register('',ProductViewSet, base_name='products')

urlpatterns = [
    *router.urls
]

