from rest_framework import serializers
from .models import ProfilePicture, Ankete, InvitationToAnkete, Invitation, OpenInfo, ClosedInfo, PasswordRestoration, Keywords

class AnketeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ankete
        fields = '__all__'

class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = "__all__"

class InvitationToAnketeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationToAnkete
        fields = '__all__'

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = '__all__'

class OpenInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenInfo
        fields = '__all__'

class ClosedInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosedInfo
        fields = '__all__'

class PasswordRestorationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordRestoration
        fields = '__all__'

class KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(required=True)
    password = serializers.CharField(required=True)