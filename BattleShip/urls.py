from django.contrib import admin
from django.urls import path

from viewer.views import SelectView, GameCreateView, GameView, GameJoinView, ShootingView, LayoutView, ResultView

from viewer.views import generate_board

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
    path('game/', GameCreateView.as_view(), name='create_game'),
    path('gamejoin/', GameJoinView.as_view(), name='game_join'),
    path('game/<game_code>', GameView.as_view(), name='game'),
    path('board', generate_board, name='board'),
    path('layout/<game_code>', LayoutView.as_view(), name='layout'),
    path('shooting/<game_code>', ShootingView.as_view(), name='shooting'),
    path('result/<game_code>', ResultView.as_view(), name='result'),
    path('select/', GameCreateView.as_view(), name='select'),
    path('account/', GameCreateView.as_view(), name='account')
    ]