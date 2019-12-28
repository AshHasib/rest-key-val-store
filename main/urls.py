from django.urls import path
from . import views

urlpatterns = [
    path('values/', views.DataAPIView.as_view()),
]