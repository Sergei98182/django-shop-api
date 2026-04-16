from django.urls import path
from .views import (
    CategoryListAPIView,
    ProductListAPIView,
    AddToCartAPIView,
    CartDetailAPIView,
    RemoveFromCartAPIView,
    ClearCartAPIView,
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),

    path('cart/add/', AddToCartAPIView.as_view()),
    path('cart/', CartDetailAPIView.as_view()),
    path('cart/remove/', RemoveFromCartAPIView.as_view()),
    path('cart/clear/', ClearCartAPIView.as_view()),
]