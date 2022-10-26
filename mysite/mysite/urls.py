from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls', namespace='homepage')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('about/', include('about.urls', namespace='about'))
]
