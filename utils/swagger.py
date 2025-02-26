from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Realmate-Challenge API",
        default_version="v1",
        description="API Docs",
    ),
    public=True,
    permission_classes=(AllowAny,)
)

swagger = schema_view.with_ui('swagger', cache_timeout=0)
