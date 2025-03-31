from rest_framework import serializers, pagination
from .models import Person, Reunion, Hobby


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('__all__')


class PersonSerializer(serializers.ModelSerializer):
    hobbies = HobbySerializer(many=True) 

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created',
        )


class ReunionSerializer(serializers.ModelSerializer):
    fecha_hora = serializers.SerializerMethodField()
    persona = PersonSerializer()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'fecha_hora',
            'persona',
        )
    
    def get_fecha_hora(self, obj):
        return str(obj.fecha) + ' - ' + str(obj.hora)


class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )
        extra_kwargs = {
            'persona': {'view_name': 'persona_app:retrieve', 'lookup_field': 'pk'}
        }


class PersonPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100


class CountReunionSerializer(serializers.Serializer):
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()
