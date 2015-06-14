from web.models import *
from web.serializers import *
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics

class ContributionViewSet(viewsets.ModelViewSet):
    serializer_class = ContributionSerializer
    queryset = Contribution.objects.all()

class ProfileViewSet(viewsets.ModelViewSet):
    seriserializer_class = ProfileSerializer
    queryset = Profile.objects.all()


