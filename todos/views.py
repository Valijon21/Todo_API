
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Toodo
from .serializers import TodoSerializer

# Create your views here.
#Toodo obyektlarni list kurinishida chiqarib beradi
class ListTodo(ListAPIView):
    queryset = Toodo.objects.all()
    serializer_class = TodoSerializer

# Bitta modelni uzini detailni yani bittasin kursatadi
class DetailTodo(RetrieveAPIView):
    queryset = Toodo.objects.all()
    serializer_class = TodoSerializer