from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url('usr/registro',views.uregistry, name='uregistry'),
]