from rest_framework import viewsets
from .models import TodoList, Pessoa
from .serializers import TodoListSerializer, PessoaSerializer

# Criando views


class TodoListViewSet(viewsets.ModelViewSet):
    # Faz uma requisição pro banco de dados e vai procurar todos os objetos do todolist
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
