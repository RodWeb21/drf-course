from rest_framework import generics, mixins
from .models import Person
from .serializers import PersonSerializer


class PersonListAPIView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonCreateAPIView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDestroyAPIView(generics.DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonUpdateAPIView(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListMixin(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PersonCreateMixin(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PersonRetrieveMixin(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PersonUpdateMixin(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PersonDestroyMixin(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PersonListCreateMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
