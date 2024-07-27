from django.urls import path
from authentication.views import SignInView, SignUpView, SignOutView


app_name = "authentication"
urlpatterns = [
    path("signin/", SignInView.as_view(), name="signin"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signout/", SignOutView, name="signout"),
]
