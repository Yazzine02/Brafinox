from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home or another page after registration
        else:
            # Even if the form is invalid, you still need to return a response with errors
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()  # When it's a GET request, show the empty form

    # Return the form (GET request or if POST request fails validation)
    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        #username = request.POST.get('username')
        #password = request.POST.get('password')
        
        print(f"Username: {username}, Password: {password}")  # Ajoutez ceci pour voir les données dans la console
        
        if username == "admin" and password == "admin":  # Authentification basique
            print("Connexion réussie")  # Pour voir si la condition est remplie
            return redirect('choice')  # Redirection vers 'choice'
        else:
            print("Erreur d'authentification")  # Vérifiez si vous avez une erreur
            return render(request, 'login.html', {'error': 'Nom d\'utilisateur ou mot de passe incorrect'})
    
    return render(request, 'login.html')

def choice_view(request):
    return render(request, 'choice.html')
