from django.urls import path
from . import views

urlpatterns = [
    #path('values/',views.GetDataListView.as_view()),
    path('values/', views.DataAPIView.as_view()),
]