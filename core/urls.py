from django.urls import path
from . import views

#nuovalista#

urlpatterns = [
    #homeURl -> empty va sul file views e chiama index
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='settings')

]
