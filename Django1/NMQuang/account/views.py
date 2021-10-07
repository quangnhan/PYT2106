from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from .forms import QuickSignUpForm


User = get_user_model()


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class QuickSignUpView(FormView):
    form_class = QuickSignUpForm
    template_name = 'registration/quicksignup.html'
    success_url = reverse_lazy('quicksignup')

    def form_invalid(self, form):
        print("form_invalid", form.cleaned_data)
        return super().form_invalid(form)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        return super().form_valid(form)
