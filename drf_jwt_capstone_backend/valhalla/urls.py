from django.urls import path
# from drf_jwt_capstone_backend.valhalla.models import RegisterUser
# from drf_jwt_capstone_backend.valhalla.views import Login
from valhalla import views 

urlpatterns = [
    path('all/', views.get_all_coffee),
    path('login/', views.login),
    path('register/', views.register),
]