from django.urls import path, include
import mainapp.views as mainapp
app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('about_me/', mainapp.about_me, name='about_me'),
     path('date/', mainapp.date, name='date'),
]


