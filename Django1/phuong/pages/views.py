from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "apps/pages/home.html"