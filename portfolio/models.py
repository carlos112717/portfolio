from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    author = models.CharField(max_length=100, verbose_name="Autor")
    description = models.TextField(verbose_name="Descripción")
    link = models.URLField(null=True, blank=True, verbose_name="Enlace")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    # Devuelve el nombre del proyecto real

    def __str__(self) -> str:
        return self.title
