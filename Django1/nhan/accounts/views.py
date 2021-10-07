from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
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
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        get_user_model().objects.create_user(
            username=email,
            email=email,
            password=password
        )

        return super().form_valid(form)