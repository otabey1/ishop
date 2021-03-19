from django.urls import path
from .views import RegistrationView, LoginView, LogoutView

app_name = 'client'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout")
]
