from dataclasses import fields
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.forms import ValidationError
from rest_framework import serializers
from teacher.models import Aula, Professor

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'#('id','name','value', 'description', 'photo')

class CadastrarAulaSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length = 255)
    name = serializers.CharField(max_length = 100)
    def validate_name(self, value):
        if len(value)<3:
            raise ValidationError("Deve ter pelo menos três caracteres")
        return value


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'