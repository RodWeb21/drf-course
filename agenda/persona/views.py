from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from .models import Person
from .serializers import PersonSerializer


class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializer


class PersonRetrieveView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonDestroyView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()