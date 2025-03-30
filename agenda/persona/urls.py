from django.urls import path
from . import views

urlpatterns = [
    path('api/persona/list/', views.PersonListAPIView.as_view()),
    path('api/persona/create/', views.PersonCreateAPIView.as_view()),
    path('api/persona/retrieve/<pk>', views.PersonRetrieveAPIView.as_view()),
    path('api/persona/destroy/<pk>', views.PersonDestroyAPIView.as_view()),
    path('api/persona/update/<pk>', views.PersonUpdateAPIView.as_view()),
    path('api/persona/retrieve-update/<pk>', views.PersonRetrieveUpdateAPIView.as_view()),
    path('api/persona/list-create/', views.PersonListCreateAPIView.as_view()),
    path('api/persona/retrieve-destroy/<pk>/', views.PersonRetrieveDestroyAPIView.as_view()),
    path('api/persona/retrieve-update-destroy/<pk>/', views.PersonRetrieveUpdateDestroyAPIView.as_view()),
    path('api/persona/list-mixin/', views.PersonListMixin.as_view()),
    path('api/persona/create-mixin/', views.PersonCreateMixin.as_view()),
    path('api/persona/retrieve-mixin/<pk>', views.PersonRetrieveMixin.as_view()),
    path('api/persona/update-mixin/<pk>', views.PersonUpdateMixin.as_view()),
    path('api/persona/destroy-mixin/<pk>', views.PersonDestroyMixin.as_view()),
    path('api/persona/list-create-mixin/<pk>', views.PersonListCreateMixin.as_view()),
    path('api/persona/retrieve-update-mixin/<pk>', views.PersonRetrieveUpdateMixin.as_view()),
]
