from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
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
