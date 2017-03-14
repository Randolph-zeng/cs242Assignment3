from django.conf.urls import url
from svnShowcase import views

urlpatterns = [
    url(r'^portfolio/$', views.getPortfolio),
]