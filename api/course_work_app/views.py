from rest_framework import viewsets
from .models import Ankete, InvitationToAnkete, Invitation, OpenInfo, ClosedInfo, PasswordRestoration, Keywords
from .serializers import LoginSerializer, AnketeSerializer, InvitationToAnketeSerializer, InvitationSerializer, OpenInfoSerializer, ClosedInfoSerializer, PasswordRestorationSerializer, KeywordsSerializer
from .models import Ankete
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from .serializers import LoginSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import LoginSerializer


class AnketeViewSet(viewsets.ModelViewSet):
    queryset = Ankete.objects.all()
    serializer_class = AnketeSerializer


@api_view(['POST'])
@permission_classes([AllowAny])  # Allow unauthenticated users to access this view
@swagger_auto_schema(
    request_body=LoginSerializer,
    operation_description="Authenticate user",
    responses={200: openapi.Response('Success'), 400: 'Invalid input', 401: 'Unauthorized'},
) # Provide schema information to Swagger
def login_view(request):
    """
    Authenticate a user and generate an authentication token.
    """
    serializer = LoginSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    login = serializer.validated_data['login']
    password = serializer.validated_data['password']

    try:
        ankete = Ankete.objects.get(login=login, password=password)
        return Response({'success': True,'ankete_id': ankete.ankete_id }, status=status.HTTP_200_OK)
    except Ankete.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


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
from .models import Ankete
