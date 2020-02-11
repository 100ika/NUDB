from django.urls import path
from . import views

urlpatterns = [
    path('', views.EquipmentView.as_view()),
]
