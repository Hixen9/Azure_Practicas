from rest_framework import serializers
from .models import Imagenes

class ImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = ["id","nombre","imagen"]