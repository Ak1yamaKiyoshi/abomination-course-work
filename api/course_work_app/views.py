from rest_framework import viewsets
from .models import Ankete, InvitationToAnkete, Invitation, OpenInfo, ClosedInfo, PasswordRestoration, Keywords
from .serializers import AnketeSerializer, InvitationToAnketeSerializer, InvitationSerializer, OpenInfoSerializer, ClosedInfoSerializer, PasswordRestorationSerializer, KeywordsSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Ankete


class AnketeViewSet(viewsets.ModelViewSet):
    queryset = Ankete.objects.all()
    serializer_class = AnketeSerializer

class InvitationToAnketeViewSet(viewsets.ModelViewSet):
    queryset = InvitationToAnkete.objects.all()
    serializer_class = InvitationToAnketeSerializer

class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

class OpenInfoViewSet(viewsets.ModelViewSet):
    queryset = OpenInfo.objects.all()
    serializer_class = OpenInfoSerializer

class ClosedInfoViewSet(viewsets.ModelViewSet):
    queryset = ClosedInfo.objects.all()
    serializer_class = ClosedInfoSerializer

class PasswordRestorationViewSet(viewsets.ModelViewSet):
    queryset = PasswordRestoration.objects.all()
    serializer_class = PasswordRestorationSerializer

class KeywordsViewSet(viewsets.ModelViewSet):
    queryset = Keywords.objects.all()
    serializer_class = KeywordsSerializer
