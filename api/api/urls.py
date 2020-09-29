"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

openapi_schema = get_schema_view(
    title="CanAirIO Services",
    version="1.0.0",
    description="API for all CanAirIO services",
    #authentication_classes=[],
    #permission_classes=[],
)

doc_schema = TemplateView.as_view(
    template_name='doc.html',
    extra_context={'schema_url': 'openapi-schema'}
)

urlpatterns = [
    path('openapi/', openapi_schema, name='openapi-schema'),
    path('doc/', doc_schema, name='doc-schema'),
    path('admin/', admin.site.urls),
    path('api/token-auth/', obtain_jwt_token),
    path('api/token-refresh/', refresh_jwt_token),
    path('api/token-verify/', verify_jwt_token),
    path('api/', include('admin_influxdb.urls')),
    path('api/', include('canairio_user.urls')),
    path('api/', include('canairio_station.urls')),
]
