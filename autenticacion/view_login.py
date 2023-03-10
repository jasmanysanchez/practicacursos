from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def loginView(request):
    data = {
        "title": "Inicia sesión"
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Nombre de usuario o contraseña no son correctos')
            return redirect('/login/')
    elif request.method == 'GET':
        return render(request, 'login.html', data)

def logoutView(request):
    logout(request)
    return redirect('/')