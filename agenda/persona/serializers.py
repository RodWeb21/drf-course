from rest_framework import serializers
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
    persona = PersonSerializer()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )
