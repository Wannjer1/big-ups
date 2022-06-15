


from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('bio','email','avatar','user')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('webimage','name','description','link','profile')