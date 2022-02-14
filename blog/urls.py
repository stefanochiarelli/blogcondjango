
from unicodedata import name
from django.urls import path
from .views import inicio_handler, all_posts, postDestalle, editPost, editarPerfil, crearPost, eliminarPost, sobreMi

urlpatterns = [
    path("", inicio_handler.as_view(), name="blog-inicio"),
    path('posts/', all_posts.as_view(), name="allposts"),
    path('posts/<slug:slug>', postDestalle.as_view(), name="post-handler"),
    path('posts/<slug:slug>/eliminar', eliminarPost.as_view(), name="post-handler-delete"),
    path('editar/<post_id>', editPost, name="edit-post" ),
    path('editarPerfil/', editarPerfil, name="editar-perfil"),
    path('crearpost/', crearPost.as_view(), name="create-post"),
    path('sobreMi/', sobreMi, name="about"),
]