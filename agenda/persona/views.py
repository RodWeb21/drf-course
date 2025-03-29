from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Person
from .serializers import PersonSerializer


class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializer
