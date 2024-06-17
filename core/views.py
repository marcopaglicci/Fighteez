from django.shortcuts import render, redirect

from django.contrib import messages
# importi la funzionalità per message front end

from django.contrib.auth.models import User, auth
# importo il modello per utente e autenticazione utente

from django.http import HttpResponse

from core.models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.

# Verify the user is already logged
@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')


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

                # vogliamo creare un profilo insieme all'user

                # TODO log user in and redirect to setting page

                # vogliamo l'oggetto user per poter creare il profilo
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)

                # salviamo il profilo e rindirizziamo alla pagina di creazione e gestione profilo
                new_profile.save()
                return redirect('signup')  # todo create log in page
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

def settings(request):



# Verify the user is already logged
@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')
