from django.conf.urls import url
from portfolio import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
