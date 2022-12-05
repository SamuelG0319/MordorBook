from django.contrib import admin
<<<<<<< HEAD
from .models import Profile, Post, LikePost, FollowersCount, Contact
=======
from .models import Profile, Post, LikePost, Comment, FollowersCount
>>>>>>> main

admin.site.register(Profile)

admin.site.register(Post)

admin.site.register(LikePost)

admin.site.register(FollowersCount)

<<<<<<< HEAD
@admin.register(Contact) #Creamos una función para ver la información desde el panel de admin.
class ContactAdmin(admin.ModelAdmin): #Damos nombre a la función.
	list_display = ('name', 'email') #Campos visibles desde el panel de administrador con respecto a los contactos.
=======
admin.site.register(Comment)
>>>>>>> main

# Register your models here.
