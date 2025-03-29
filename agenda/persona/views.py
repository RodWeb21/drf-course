from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import Person
from .serializers import PersonSerializer


class PersonListAPIView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class PersonCreateAPIView(CreateAPIView):
    serializer_class = PersonSerializer


class PersonRetrieveAPIView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonDestroyAPIView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonUpdateAPIView(UpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonListCreateAPIView(ListCreateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
