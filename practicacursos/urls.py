"""practicacursos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from autenticacion.view_login import loginView, logoutView
from autenticacion.view_register import registerView
from curso.view_cursosinscrito import cursosInscritoView
from practicacursos import settings
from curso.view_cursos import cursosView
from curso.view_inscribirse import inscribirseView
from informacion.view_acercade import acercaDeView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cursosView),
    path('inscribirse/<int:curso_id>/', inscribirseView),
    path('login/', loginView),
    path('logout/', logoutView),
    path('acerca-de/', acercaDeView),
    path('register/', registerView),
    path('cursos-inscrito/', cursosInscritoView),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
