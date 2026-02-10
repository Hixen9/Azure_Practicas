from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Imagenes
from .serializers import ImagenesSerializer
from rest_framework.permissions import AllowAny

class ImagenesViewSet(ModelViewSet):
    queryset = Imagenes.objects.all()
    serializer_class = ImagenesSerializer
    permission_classes = [AllowAny]
# Create your views here.
