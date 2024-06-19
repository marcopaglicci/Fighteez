from django.urls import path
from . import views

# nuovalista#

urlpatterns = [
    # homeURl -> empty va sul file views e chiama index
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('like-post', views.like_post, name='like-post'),
    path('follow', views.follow, name='follow'),
    path('profile/<str:pk>', views.profile, name='profile')
    # profile/<str:pk>permette di avere la primarykey dell'user come parte dell'url


]
