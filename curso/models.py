from django.db import models
from django.core.validators import FileExtensionValidator

class Curso(models.Model):
    foto = models.FileField("Imagen", upload_to="cursos/", validators=[FileExtensionValidator(["jpg", "png", "jpeg", "webp"])])
    nombre = models.CharField("Nombre del curso", max_length=255)
    descripcion = models.TextField("Describe el curso")
    cupo = models.PositiveIntegerField("Cupo disponible")
    precio = models.DecimalField("Precio", decimal_places=2, max_digits=30)
    mensaje_promocion = models.TextField("Mensaje para promoción (Opcional)", max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.cupo} - ${self.precio}"
    
    def get_cupo(self):
        return (self.cupo - InscritoCurso.objects.filter(curso_id=self.id).count())
    

class InscritoCurso(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.PROTECT, verbose_name="Usuario")
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso")
    precio = models.DecimalField("Precio", decimal_places=2, max_digits=30)
    impuestos = models.DecimalField("Impuestos", decimal_places=2, max_digits=30)
    total = models.DecimalField("Total", decimal_places=2, max_digits=30)
    fecha_registro = models.DateTimeField("Fecha de registro", auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.curso.nombre} - ${self.total}"