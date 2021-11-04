from django.urls import path
from valhalla import views

urlpatterns = [
    path('all/', views.get_all_coffee)
]