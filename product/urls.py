from django.urls import path
from .views import (
    CategoryListAPIView,
    CategoryDetailAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    ReviewListAPIView,
    ReviewDetailAPIView
)

from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryListAPIView.as_view(), name="category_list"),
    path("categories/<int:id>/", views.CategoryDetailAPIView.as_view(), name="category_detail"),

    path("products/", views.ProductListAPIView.as_view(), name="product_list"),
    path("products/<int:id>/", views.ProductDetailAPIView.as_view(), name="product_detail"),

    path("reviews/", views.ReviewListAPIView.as_view(), name="review_list"),
    path("reviews/<int:id>/", views.ReviewDetailAPIView.as_view(), name="review_detail"),
]
