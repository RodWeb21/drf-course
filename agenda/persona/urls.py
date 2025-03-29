from django.urls import path
from . import views

urlpatterns = [
    path('api/persona/list/', views.PersonListApiView.as_view()),
    path('api/persona/create/', views.PersonCreateView.as_view()),
]
