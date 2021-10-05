from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from .forms import FastSignupForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class FastSignupView(FormView):
    form_class = FastSignupForm
    template_name = 'registration/fast_signup.html'
    success_url = reverse_lazy('fast_signup')

    def form_invalid(self, form):
        print("form_invalid", form.cleaned_data)
        return super().form_invalid(form)

    def form_valid(self, form):
        print("form_valid", form.cleaned_data)
        return super().form_valid(form)