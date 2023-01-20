from django.urls import path
from .views import SneakerModelsListView, SneakerModelsDetailView

urlpatterns = [
    path('', SneakerModelsListView.as_view()),
    path('<int:pk>/', SneakerModelsDetailView.as_view())
]