from django.contrib import admin
from django.urls import path
from register.views import register,home
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', register, name="register"),
    path('login/', LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

