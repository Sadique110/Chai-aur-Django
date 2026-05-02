from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
 
# localhost:8000/chai
# localhost:8000/chai/order
urlpatterns = [
    path('', views.all_chai, name='chai/all_chai'),
]