from rest_framework  import serializers
from .models import Toodo

class ToodoSerialezer(serializers.ModelSerializer):
    class Meta:
        model = Toodo
        fields = ('id','title','body')