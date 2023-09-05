from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from .forms import NewUserForm, ProfileForm
from .models import Profile


def register_request(request):
    if not Group.objects.filter(name='Customer').exists():
        Group.objects.create(name='Customer')

    customer_group = Group.objects.get(name='Customer')
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(customer_group)
            user.save()

            new_profile = Profile.objects.create(user=user, username=user.username)

            login(request, user)
            messages.success(request, "Регистрация прошла успешно")
            return redirect('location_page')
        else:
            messages.error(request, "Ошибка. Неверно введенная информация")

    form = NewUserForm()
    return render(request, 'registration_page.html', context={'registration_form': form})


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            new_username = form.cleaned_data['username']
            if new_username != request.user.username:
                request.user.username = new_username
                request.user.save()
            form.save()
            return redirect('profile')

    return render(request, 'profile.html', {'profile': profile, 'form': form})


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Профиль успешно удален')
        logout(request)
        return redirect('login')
    return render(request, 'delete_profile.html')

# def register_request(request):
#     return HttpResponse('TYTYTYTYTYT')
