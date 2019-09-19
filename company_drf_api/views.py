from rest_framework import viewsets

from .models import User, CompanyProfile
from .serializers import UserSerializer, CompanySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanySerializer