from django.urls import path
from users import views as users_views

urlpatterns = [
    path('signup/', users_views.signup_view, name='signup'),
    path('login', users_views.user_login, name='login'),
    path('logout/', users_views.user_logout, name='logout')
]
