from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from autenticacion.forms import RegisterUserForm

def registerView(request):
    data = {
        "title": "Registrarse"
    }
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/login/')
        else:
            for k, v in form.errors.items():
                messages.error(request, v[0])
            return redirect(request.path)
    elif request.method == 'GET':
        data['form'] = RegisterUserForm()
        return render(request, 'register.html', data)