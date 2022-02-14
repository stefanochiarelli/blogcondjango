



from django.http import  HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Post
from .forms import CommentForm, PostForm, UserEditForm
# from django.views.generic.detail import DetailView
from django.views.generic import View
from django.views.generic import ListView, CreateView, DeleteView


class inicio_handler(ListView):
    model = Post
    template_name = "blog/index.html"    
    context_object_name = "lista"

   

    def get_queryset(self):
        queryset = super().get_queryset()
        data_posts = queryset[:3]
        return data_posts


class all_posts(ListView):
    model = Post
    template_name = "blog/allposts.html"    
    context_object_name = "lista"

    



class postDestalle(View):
    
    def get(self, response, slug):
        post = Post.objects.get(slug=slug)
        # usuario_activo = response.user
        
        context = {
            'detail': post,
            'form': CommentForm(),
            'comentarios': post.post_comments.all(),
            'tags': post.tags.all()
            
            
        }
        
        return render(response, 'blog/detalle-post.html', context)

    def post(self, response, slug):
        comment_form = CommentForm(response.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.usuario = response.user
            comment.usuario_post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-handler', args=[slug]))

        context = {
            'detail': post,
            'form': CommentForm(),
            'comentarios': post.post_comments.all()
            
        }
        return render(response, 'blog/detalle-post.html', context)

#view edit post

def editPost(request, post_id):
    post_to_update = Post.objects.get(slug=post_id)
    post_form = PostForm(request.POST or None ,instance=post_to_update)

    if post_form.is_valid():
        post_form.save()
        return redirect('blog-inicio')

    context = {
        'to_update': post_to_update,
        'form': post_form 
    
    }
    return render(request, 'blog/update-posts.html', context)



#Crear nuevo Post
class crearPost(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'blog/create-post.html'
    
        



def editarPerfil(request):

    #Instancia del login
    usuario = request.user

    #Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid():   #Si pasó la validación de Django

                informacion = miFormulario.data
            
                #Datos que se modificarán
                usuario.username = informacion['username']
                usuario.email = informacion['email']
                usuario.password1 = informacion['password1']
                usuario.password2 = informacion['password1']
                usuario.first_name = informacion['first_name']
                usuario.last_name = informacion['last_name']
                usuario.save()

            return render(request, "blog/index.html") #Vuelvo al inicio o a donde quieran
    #En caso que no sea post
    else: 
        #Creo el formulario con los datos que voy a modificar
        miFormulario= UserEditForm(initial={ 'email':usuario.email, 'username': usuario.username, 'first_name': usuario.first_name, 'last_name': usuario.last_name}) 

        #Voy al html que me permite editar
        return render(request, "blog/editarPerfil.html", {"formUser":miFormulario, "usuario":usuario})


class eliminarPost(DeleteView):
    model = Post
    template_name = 'blog/delete-post.html'
    success_url = reverse_lazy('blog-inicio')


def sobreMi(request):
    return render(request, 'blog/about.html')  