from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions, authentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="UNIVERSITY OF ZIMBABWE BACKEND API",
        default_version='v1',
        description="UNIVERSITY OF ZIMBABWE RECRUITMENT PORTAL BACKEND API",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
    authentication_classes=[]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/institutions/', include('institution.urls')),
    path('api/v1/superusers/', include('superusers.urls')),
    path('api/v1/administrators/', include('administrators.urls')),
    path('api/v1/applicants/', include('applicants.urls')),
    path('api/v1/work-experiances/', include('applicants.work_experiances.urls')),
    path('api/v1/applicant-docs/', include('applicants.applicant_docs.urls')),
    path('api/v1/educational-qualifications/', include('applicants.educational_qualifications.urls')),
    path('api/v1/job-categories/', include('job_categories.urls')),
    path('api/v1/jobs/', include('jobs.urls')),
    path('api/v1/skills/', include('skills.urls')),
    path('api/v1/applicant-skills/', include('applicant_skills.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
