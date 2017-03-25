from django.conf.urls import url
from svnShowcase import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^portfolio/$', views.getPortfolio),
		url(r'^home/$', TemplateView.as_view(template_name="index.html")),
		url(r'^files/', TemplateView.as_view(template_name="files.html")),
]
