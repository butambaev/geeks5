from django.urls import path
from .views import ( CategoryListCreateView, CategoryDetailView, ProductListCreateView,ProductDetailView, ProductWithReviewsView, ReviewListCreateView,ReviewDetailView,)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),

    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('products/reviews/', ProductWithReviewsView.as_view()),

    path('reviews/', ReviewListCreateView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailView.as_view()),
]
