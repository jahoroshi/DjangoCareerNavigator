from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Recruitment Assistant API",
        default_version='v1',
        description="Документация API для приложения Recruitment Assistant",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/candidate/', include('api.candidate.urls')),
    path('api/recruiter/', include('api.recruiter.urls')),
    path('api/job/', include('api.job.urls')),
    path('api/matching/', include('api.matching.urls')),
    path('api/authentication/', include('api.authentication.urls')),  # Создадим отдельно для аутентификации

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # ReDoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

