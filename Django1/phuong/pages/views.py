from django.views.generic import TemplateView
from django.views.generic import Lo
# Create your views here.

class HomePageView(TemplateView):
    template_name = "apps/pages/home.html"