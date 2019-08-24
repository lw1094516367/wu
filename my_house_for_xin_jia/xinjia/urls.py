from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'info_reveal', views.info_reveal, name='info_reveal'),
    url(r'register', views.register, name='register'),
]