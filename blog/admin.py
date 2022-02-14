import imp
from django.contrib import admin

from .models import Post, Autor, Tag, CommentModel

# Register your models here.


admin.site.register(Post)
admin.site.register(Autor)
admin.site.register(Tag)
admin.site.register(CommentModel)