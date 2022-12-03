from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount, Contact

admin.site.register(Profile)

admin.site.register(Post)

admin.site.register(LikePost)

admin.site.register(FollowersCount)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')

# Register your models here.
