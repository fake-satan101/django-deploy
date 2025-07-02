from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .forms import Userform,Profile_form,Log_in
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, "first_app/index.html")
@login_required
def special(request):
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user:
            if user.is_active:

                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse('User is not active!')
        else:
            print("Someone with Username: {} and password: {} tried to login!".format(username,password))
            return HttpResponse("invalid username or password!")


    return render(request,'first_app/login.html',{})
def form(request):
    registered = False

    if request.method == "POST":
        user_form = Userform(request.POST)
        profile_form = Profile_form(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid() :
            if user_form.cleaned_data['password']!=user_form.cleaned_data['password_again']:
                user_form.add_error(None, "Passwords do not match.")
            else:
                user = user_form.save()
                user.set_password(user.password)  # Hash the password
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user  # Link the profile to the user
                if 'profile_pic' in request.FILES:
                    # If yes, then grab it from the POST form reply
                    profile.profile_pic = request.FILES['profile_pic']
                profile.save()

                registered = True

    else:
        user_form = Userform()
        profile_form = Profile_form()

    return render(request, "first_app/form.html", {
        "form": user_form,
        "profile": profile_form,
        "registered": registered
    })
def log_in(request):

    if request.method == "POST":
        form = Log_in(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, "first_app/form.html", {"msg": "Login Success!"})
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = Log_in()

    return render(request, "first_app/form.html", {"form": form})
