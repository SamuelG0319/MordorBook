from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount, Contact

admin.site.register(Profile)

admin.site.register(Post)

admin.site.register(LikePost)

admin.site.register(FollowersCount)

@admin.register(Contact) #Creamos una función para ver la información desde el panel de admin.
class ContactAdmin(admin.ModelAdmin): #Damos nombre a la función.
	list_display = ('name', 'email') #Campos visibles desde el panel de administrador con respecto a los contactos.

# Register your models here.
