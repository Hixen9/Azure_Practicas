from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Imagenes
from .serializers import ImagenesSerializer

class ImagenesViewSet(ModelViewSet):
    query = Imagenes.objects.all().order_by("-id")
    serializer_class =ImagenesSerializer
# Create your views here.
