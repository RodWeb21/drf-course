from django.urls import path
from . import views

urlpatterns = [
    path('api/persona/list/', views.PersonListApiView.as_view()),
]
