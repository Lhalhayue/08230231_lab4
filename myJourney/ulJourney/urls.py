from django.contrib import admin
from django.urls import path
from ulJourney import views  # import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),          # Homepage
    path('about/', views.about_me, name='about_me'),  # About Me page
]
