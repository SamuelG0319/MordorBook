from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
import uuid
from datetime import datetime

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #usamos una foreign key
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):

    class meta:
        ordering = ['date']#Ordenamos datos por medio de la fecha.

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(blank=True, null=True) #Creamos la variable para guardar la fecha y asignamos su tipo de dato.

    def __str__(self):
        return self.user
    
    #Función que permite guardar los datos en un slug para hacerlos visibles cuando se entre a un URL referido.
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.id, self.commenter_name)

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

class Contact(models.Model): #Creación del modelo para guardar los datos de contacto.

    class Meta:
        verbose_name = 'Contact' #Nombre singular para el campo en la sección de administración.
        verbose_name_plural = 'Contacts' #Nombre plurarl para el campo en la sección de administración.

    name = models.CharField(max_length=100, blank=True, null=True) #Creamos la variable para guardar el autor y asignamos su tipo de dato.
    email = models.EmailField(max_length=100, blank=True, null=True) #Creamos la variable para guardar el correo y asignamos su tipo de dato.
    message = models.CharField(max_length=100, blank=True, null=True) #Creamos la variable para guardar el mensaje y asignamos su tipo de dato.

    #Función para representar los objetos de clase como una cadena.
    def __str__(self):
        return self.name


# Create your models here.
