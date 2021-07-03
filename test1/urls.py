from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='main')),
    path('about_me/', include('mainapp.urls', namespace='about_me')),
     path('date/', include('mainapp.urls', namespace='date')),
]
