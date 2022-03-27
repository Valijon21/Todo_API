from msilib.schema import ServiceInstall
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Toodo
from .serializers import ToodoSerializer

# Create your views here.
#Toodo obyektlarni list kurinishida chiqarib beradi
class ListToodo(ListAPIView):
    queryset = Toodo.objects.all()
    serailizer_class = ToodoSerializer

# Bitta modelni uzini detailni yani bittasin kursatadi
class DetailToodo(RetrieveAPIView):
    queryset = Toodo.objects.all()
    serializer_class = ToodoSerializer