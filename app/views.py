from django.shortcuts import render
from rest_framework import generics, permissions
from .models import BasicInfo
from .serializers import BasicInfoSerializer
# Create your views here.
def home(request):
    return render(request, 'index.html', {})

class BasicInfoCreateView(generics.CreateAPIView):
    queryset = BasicInfo.objects.all()
    serializer_class = BasicInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class BasicInfoListView(generics.ListAPIView):
    queryset = BasicInfo.objects.all()
    serializer_class = BasicInfoSerializer
    http_method_names = ['get']