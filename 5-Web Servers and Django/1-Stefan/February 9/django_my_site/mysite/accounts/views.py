from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        # criar um formulario e populalo com o que esta no corpo do request
        form = LoginForm(request.POST)
        # verifica se o formulario esta válido
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet (commit=False)
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password( # automaticamente processa o hashing
                user_form.cleaned_data['password']) #hashing - transforma a pass para um valor, sem guardar a pass original
            # Save the User object
            new_user.save()
            # Create the user profile, e guarda na BD
            Profile.objects.create(user=new_user)
            return render(request,
                          'accounts/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'accounts/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        # criamos os dois formularios
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        # verifica a validade
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, 'Profile updated successfully')
        # else:
            # messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'accounts/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


def profile(request, profile_id):
    user_profile = get_object_or_404(Profile, id=profile_id)
    user = get_user_model().objects.get(id=user_profile.user_id)

    return render(request,
                  'accounts/profile.html',
                  {'profile': user_profile,
                   'user': user})

