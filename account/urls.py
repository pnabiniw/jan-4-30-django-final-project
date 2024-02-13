from django.urls import path
from .views import user_logout, UserLoginView, UserRegister

urlpatterns = [
    path('logout/', user_logout, name="user_logout"),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('register/', UserRegister.as_view(), name='user_register')
]
