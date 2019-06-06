from django.urls import path

from . import views

urlpatterns = [
    path('', views.ParticularsList.as_view()),
    path('<int:pk>/', views.ParticularsDetail.as_view()),
]