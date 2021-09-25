from django.contrib import admin
from django.urls import path

from viewer.views import TestView

from viewer.views import generate_demo

from accounts.views import SubmittableLoginView, SubmittablePasswordChangeForm, SignUpView

from django.contrib.auth import views



urlpatterns = [
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('admin/', admin.site.urls),
]