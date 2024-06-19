from django.shortcuts import render, redirect

from django.contrib import messages
# importi la funzionalità per message front end

from django.contrib.auth.models import User, auth
# importo il modello per utente e autenticazione utente

from django.http import HttpResponse

from core.models import Profile, Post, LikePost, FollowersCount
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

from itertools import chain

# Create your views here.

# Verify the user is already logged
@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    user_following_list = []
    feed = []

    user_following = FollowersCount.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_list = Post.objects.filter(user=usernames)
        feed.append(feed_list)

    feed_list = list(chain(*feed))

    posts = Post.objects.all()
    return render(request, 'index.html', {'user_profile': user_profile, 'posts': feed_list})


def signup(request):
    # if request cames form POST method (so not by opening the page)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'This Email is Already Used')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'This Username is Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # log in user e rindirizamento su settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # vogliamo l'oggetto user per poter creare il profilo
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)

                # salviamo il profilo e rindirizziamo alla pagina di creazione e gestione profilo
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')

    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password Not Matching')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':

        # se l'utente non ha inserito nessuna nuova immagine
        if request.FILES.get('image') is None:
            image = user_profile.profile_img
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profile_img = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        if request.FILES.get('image') is not None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profile_img = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        return redirect('settings')
    return render(request, 'setting.html', {'user_profile': user_profile})


@login_required(login_url='signin')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')

    else:
        return redirect('')


@login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    # controlliamo se il post ha gia un like dall'user
    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter is None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.num_of_likes = post.num_of_likes + 1
        post.save()
        return redirect("/")
    else:
        like_filter.delete()
        post.num_of_likes = post.num_of_likes - 1
        post.save()
        return redirect("/")


@login_required(login_url='signin')
def profile(request, pk):
    # nell' url viene passata anche la pk dell' utente che quindi fa parte degli argomenti della view
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_post = Post.objects.filter(user=pk)
    user_post_lenght = len(user_post)

    follower = request.user.username
    user = pk

    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_following = len(FollowersCount.objects.filter(follower=pk))

    # dato che passo molte informazioni diverse a profile.html è importante farlo con un "contest"
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_post': user_post,
        'user_post_lenght': user_post_lenght,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following
    }
    return render(request, 'profile.html', context)


# Verify the user is already logged
@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/profile/' + user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/' + user)
    else:
        return redirect("/")

