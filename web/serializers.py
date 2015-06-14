from rest_framework import serializers
from web.models import *

class ProfileSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Profile
        fields = ('id', 'nick', 'photo')

class ContributionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ('id', 'user', 'description')





