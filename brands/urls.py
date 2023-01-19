from django.urls import path 
from .views import BrandListView, BrandDetailView 

urlpatterns = [
    path('', BrandListView.as_view()),
    path('<int:pk>/', BrandDetailView.as_view())
]