from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('s/', views.set_session_view),
    path('g/', views.get_session_view),
    path('d/', views.delete_session_view),
]