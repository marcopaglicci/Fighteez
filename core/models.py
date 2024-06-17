from django.db import models

from django.contrib.auth import get_user_model
#questo import ci permette di ottenere l'user autenticato in quel momento nel sistema

User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank = True)
    location = models.CharField(max_length=100, blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default= 'blank_profile_picture.png')

                                                                            #Imagefield("here") segna dove va l'immagine ,
                                                                            # nel nostro caso con l'upload vogliamo una zona
                                                                            # dove caricare i file per gli user, dato che abbiamo
                                                                            #fatto un set per la cartella media Django andrà a cercare li i file
    def __str__(self):
        return self.user.username
