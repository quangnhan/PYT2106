from django.urls import path
from .views import (
    QuickSignUpView,
    SignUpView,
)

urlpatterns = [
    path('signup', SignUpView.as_view(), name="signup"),
    path('quicksignup', QuickSignUpView.as_view(), name="quicksignup"),
]
