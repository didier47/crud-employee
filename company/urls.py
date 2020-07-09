from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from polaris.common.utilities import CustomOpenAPISchemaGenerator
from rest_framework.routers import SimpleRouter

from company.settings import SWAGGER_URL, BASE_URL
from employee.views import EmployeeViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Compañía",
        default_version='v1',
        description="Crud de empleados"
    ),
    generator_class=CustomOpenAPISchemaGenerator,
    public=True,
    url=SWAGGER_URL
)

router = SimpleRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path(BASE_URL, include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
