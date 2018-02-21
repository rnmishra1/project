from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^profile', views.update_profile),
    url(r'^view', views.view_profile),
    ]