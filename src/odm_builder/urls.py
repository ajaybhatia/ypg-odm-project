from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/$', views.index, name='builder_home'),
]
