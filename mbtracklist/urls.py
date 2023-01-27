from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from mbtrack import views as mbtrack_views
from list import views as list_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mbtracks', mbtrack_views.MBTrackViewSet)
router.register(r'lists', list_views.ListViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('mbtrack.urls')),
    path('', include('list.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
