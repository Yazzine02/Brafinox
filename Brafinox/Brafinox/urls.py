from django.contrib import admin
from django.urls import path
from register.views import register, home, choice_view, stock_view, client_view ,custom_login_view ,add_stock_view,view_stock_view ,export_stock_to_excel# Importez les vues nécessaires
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', custom_login_view, name='login'),  # Utilisez votre vue personnalisée
    path('logout/', LogoutView.as_view(), name='logout'),
    path('choice/', choice_view, name='choice_view'),
    path('stock/', stock_view, name='stock_view'),
    path('client/', client_view, name='client_view'),
    path('add-stock/', add_stock_view, name='add_stock_view'),
    path('view-stock/', view_stock_view, name='view_stock_view'),
     path('export_stock/', export_stock_to_excel, name='export_stock_to_excel'),
]
