from django.urls import path
from . import views
from . views import MyGoogleLoginView


urlpatterns =  [
    path('sign_up/', views.sign_up, name="sign_up"),
    path('user_login/', views.user_login, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/google/login/', MyGoogleLoginView.as_view(), name='google_login'),
]