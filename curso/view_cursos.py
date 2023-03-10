from django.shortcuts import render

from curso.models import Curso


def cursosView(request):
    data = {
        "title": "Cursos disponibles"
    }
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        data["cursos"] = Curso.objects.all()
        return render(request, 'index.html', data)