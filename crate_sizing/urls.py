from django.urls import path
from . import views
app_name = "crate_sizing"

urlpatterns = [
path('', views.shipping, name = 'Shipping'),
path('get_cutlist', views.get_cutlist, name = 'get_cutlist')
]