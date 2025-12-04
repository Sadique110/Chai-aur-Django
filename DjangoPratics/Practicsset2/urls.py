from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path ("",view.practicsset2_home,name="Practicsset2/practicsset2_home")
]    