from rest_framework import serializers
from todo.models import TodoList, Pessoa


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'  # Vai transformar todos os campos em JSON


class PessoaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome']  # forma mais bruta de importar
