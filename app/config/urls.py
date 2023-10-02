from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # rest_framework.urls for using browsable API
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/', include('apps.users.urls', namespace='users')),
    path("api/post/", include("apps.posts.urls", namespace="posts")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)