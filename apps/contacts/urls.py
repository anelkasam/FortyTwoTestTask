from django.conf.urls import  url

from apps.contacts import views

urlpatterns = [
    url(r'$', views.IndexView.as_view(), name='index'),
    ]