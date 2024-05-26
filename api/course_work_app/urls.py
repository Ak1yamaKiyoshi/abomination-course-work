from django.urls import path, include, re_path
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="CourseWorkApi",
        default_version='v1',
        description="Your API Description",
        terms_of_service="https://www.yoursite.com/policies/terms/",
        contact=openapi.Contact(email="contact@yoursite.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register('ankete', views.AnketeViewSet)
router.register('invitation-to-ankete', views.InvitationToAnketeViewSet)
router.register('invitation', views.InvitationViewSet)
router.register('open-info', views.OpenInfoViewSet)
router.register('closed-info', views.ClosedInfoViewSet)
router.register('password-restoration', views.PasswordRestorationViewSet)
router.register('keywords', views.KeywordsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
