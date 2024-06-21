from django.db import models

from django.contrib.auth import get_user_model
# questo import ci permette di ottenere l'user autenticato in quel momento nel sistema

import uuid  # permette di creare id univoci

from _datetime import datetime

User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    discipline = models.CharField(max_length=50, blank=True)
    profile_img = models.ImageField(upload_to='profile_images', default='blank_profile_picture.png')
    Professional = models.BooleanField(default=False)

    # Imagefield("here") segna dove va l'immagine ,
    # nel nostro caso con l'upload vogliamo una zona
    # dove caricare i file per gli user, dato che abbiamo
    # fatto un set per la cartella media Django andrà a cercare li i file

    def __str__(self):
        return self.user.username


class Palmares(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    professional = models.BooleanField(default=False)
    fights = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    federation = models.CharField(max_length=100, blank=True)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    num_of_likes = models.IntegerField(default=0)
    show_comments = models.BooleanField(default=True)

    def __str__(self):
        return self.user


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'Comment by {self.user} on {self.post.id}'