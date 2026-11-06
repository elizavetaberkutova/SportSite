from django.contrib import admin
from django.urls import path
from sport import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('football', views.football),
    path('hockey', views.hockey),
    path('basketball', views.basketball),
]