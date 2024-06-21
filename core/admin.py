from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount, Palmares, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'caption', 'created_at', 'image', 'num_of_likes')  # Aggiungi qui i campi che vuoi visualizzare




# Registra il modello con la classe personalizzata

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
admin.site.register(Palmares)
