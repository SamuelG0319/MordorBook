from django.contrib import admin
from .models import Profile, Post, LikePost, Comment, FollowersCount

admin.site.register(Profile)

admin.site.register(Post)

admin.site.register(LikePost)

admin.site.register(FollowersCount)

admin.site.register(Comment)

# Register your models here.
