from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from firstapp.forms import UserProfileForm, UserForm
from . import forms
#from firstapp.forms import NewUserForm
# Create your views here.

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    #my_dict = {'insert_me': "this is the bet"}
    context_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'firstapp/index.html', context_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print ("Validation success!")
            print (form.cleaned_data['name'])
            print (form.cleaned_data['email'])
            print (form.cleaned_data['text'])


    return render(request, 'firstapp/form_page.html', {'form': form})

def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error invalid')

    return render(request, 'firstapp/users.html', {'form': form})

def relative(request):
    return render(request, 'firstapp/relativeURL.html')


def register(request):
    registered = False
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():
            print('testing')
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'firstapp/registration.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active")
        else:
            print("someone tried to log in and failed")
            print("Username: {} and password{}".format(username, password))
            return HttpResponse("invalid log in")
    else:
        return render(request, 'firstapp/login.html')
