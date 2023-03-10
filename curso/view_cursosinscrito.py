from decimal import Decimal
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from curso.models import Curso, InscritoCurso
from django.contrib import messages


@login_required(login_url='/login/')
def cursosInscritoView(request):
    data = {
        "title": f"Cursos inscritos"
    }
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        data["inscritos"] = InscritoCurso.objects.filter(user_id=request.user.id)
        return render(request, 'cursos_inscrito.html', data)