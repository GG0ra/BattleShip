from django.contrib import admin
from django.urls import path

from viewer.views import SelectView, GameView

from viewer.views import generate_demo

from accounts.views import SubmittableLoginView, SubmittablePasswordChangeForm, SignUpView

from django.contrib.auth import views



urlpatterns = [
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', SubmittablePasswordChangeForm.as_view(),
         name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(),
         name='password_reset'),
    path('passwrod_reset/done/', views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done', views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('sign-up/', SignUpView.as_view(), name='sign_up'),

    path('admin/', admin.site.urls),
    path('', SelectView.as_view(), name='index'),
    path('game/', GameView.as_view(), name='game'),
    path('select/', GameView.as_view(), name='select'),
    path('account/', GameView.as_view(), name='account')
    ]