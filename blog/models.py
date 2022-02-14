from django.urls import reverse
from django.db import models




# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.caption}"


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name_plural = "Autores"



class Post(models.Model):
    titulo = models.CharField(max_length=50)
    sumario = models.CharField(max_length=150)
    nombre_imagen = models.ImageField(upload_to="post_files")
    fecha = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    contenido = models.TextField(max_length=50000, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.titulo}"

    
    def get_absolute_url(self):
        return reverse('post-handler', kwargs={"slug": self.slug })



class CommentModel(models.Model):
    usuario = models.CharField(max_length=150)
    usuario_email = models.EmailField(max_length=254)
    usuario_mensaje = models.TextField(max_length=1500)
    usuario_fecha_comment = models.DateTimeField(auto_now=True)
    usuario_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name="post_comments")

    def __str__(self):
        return f"{self.usuario_email}"




