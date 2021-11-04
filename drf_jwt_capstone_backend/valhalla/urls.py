from django.urls import path
from valhalla import views

urlpatterns = [
    path('', views.CoffeeList.as_view())
]