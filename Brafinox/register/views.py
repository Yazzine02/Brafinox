# views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'register/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie ! Vous êtes maintenant connecté.")
            return redirect("home")
        else:
            messages.error(request, "Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = CustomUserCreationForm()
    return render(request, "register/register.html", {"form": form})

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Connexion réussie !")
                return redirect('choice_view')
        else:
            messages.error(request, "Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = AuthenticationForm()
    return render(request, 'register/login.html', {'form': form})





from .forms import ProductForm
from django.contrib import messages

def add_stock_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'article a été ajouté au stock avec succès !")
            return redirect('choice_view')  # Redirige vers la vue de choix après l'ajout
        else:
            messages.error(request, "Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = ProductForm()
    return render(request, 'register/add_stock.html', {'form': form})
def choice_view(request):
    return render(request, 'register/choice.html')

def stock_view(request):
    return render(request, 'register/stock.html')  # Assurez-vous d'avoir ce fichier de modèle

def client_view(request):
    return render(request, 'register/client.html')  # Assurez-vous d'avoir ce fichier de modèle
def add_stock_view(request):
    # Logique pour ajouter au stock
    return render(request, 'register/add_stock.html')

def view_stock_view(request):
    # Logique pour voir le stock
    return render(request, 'register/view_stock.html')
