from decimal import Decimal
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from curso.models import Curso, InscritoCurso
from django.contrib import messages


@login_required(login_url='/login/')
def inscribirseView(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    data = {
        "curso": curso,
        "title": f"Inscribirse en el curso {curso.nombre}"
    }
    if request.method == 'POST':
        if not InscritoCurso.objects.filter(curso_id=curso.id, user_id=request.user.id).exists():
            impuestos = curso.precio * Decimal('0.12')
            inscrito = InscritoCurso(
                curso_id=curso.id, user_id=request.user.id, 
                precio=curso.precio, impuestos=impuestos, 
                total=impuestos + curso.precio
            )
            inscrito.save()
            return redirect('/cursos-inscrito/')
        else:
            messages.error(request, f"Ya estás inscrito en el curso {curso.nombre}")
            return redirect('/')
    elif request.method == 'GET':
        data["impuestos"] = impuestos = curso.precio * Decimal('0.12')
        data["total"] = impuestos + curso.precio
        return render(request, 'inscribirse.html', data)