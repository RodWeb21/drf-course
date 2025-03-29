from django.urls import path
from . import views

urlpatterns = [
    path('api/persona/list/', views.PersonListApiView.as_view()),
    path('api/persona/create/', views.PersonCreateView.as_view()),
    path('api/persona/retrieve/<pk>', views.PersonRetrieveView.as_view()),
    path('api/persona/destroy/<pk>', views.PersonDestroyView.as_view()),
    path('api/persona/update/<pk>', views.PersonUpdateView.as_view()),
    path('api/persona/retrieve-update/<pk>', views.PersonRetrieveUpdateView.as_view()),
]
