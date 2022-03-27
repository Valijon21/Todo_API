from rest_framework  import serializers
from .models import Toodo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toodo
        fields = ('id','title','body')