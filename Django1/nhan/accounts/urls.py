from django.urls import path
from .views import (
    SignUpView,
    FastSignupView,
)

urlpatterns = [
    path('signup', SignUpView.as_view(), name="signup"),
    path('fast-signup', FastSignupView.as_view(), name="fast_signup"),
]
