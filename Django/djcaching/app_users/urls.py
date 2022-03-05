from django.urls import path

from app_users.views import restore_password, login_view, logout_view, register_view, user_account, update_user_account

urlpatterns = [
    path('restore_password/', restore_password, name='restore_password'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('', user_account, name='user_account'),
    path('update_account/', update_user_account, name='update'),
]
