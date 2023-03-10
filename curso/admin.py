from django.contrib import admin

from curso.models import Curso, InscritoCurso

admin.site.register([Curso, InscritoCurso])