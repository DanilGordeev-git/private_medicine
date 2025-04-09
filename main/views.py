from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import ServiceCategory, Service
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm, AvatarUploadForm
from django.contrib import messages


@login_required
def profile_edit_view(request):
    user = request.user
    avatar_form = AvatarUploadForm(instance=user.profile)

    if request.method == 'POST':
        if 'avatar_submit' in request.POST:
            avatar_form = AvatarUploadForm(request.POST, request.FILES, instance=user.profile)
            if avatar_form.is_valid():
                avatar_form.save()
                messages.success(request, 'Аватар успешно обновлен!')
                return redirect('profile_edit')

        elif 'profile_submit' in request.POST:
            form = ProfileEditForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Профиль успешно обновлен!')
                return redirect('profile')
    else:
        form = ProfileEditForm(instance=user)

    return render(request, 'main/profile_edit.html', {
        'form': form,
        'avatar_form': avatar_form
    })

@login_required
def profile_view(request):
    user = request.user
    avatar_form = AvatarUploadForm(instance=user.profile)

    if request.method == 'POST':
        if 'avatar_submit' in request.POST:
            avatar_form = AvatarUploadForm(request.POST, request.FILES, instance=user.profile)
            if avatar_form.is_valid():
                avatar_form.save()
                messages.success(request, 'Аватар успешно обновлен!')
                return redirect('profile')

        elif 'profile_submit' in request.POST:
            form = ProfileEditForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Профиль успешно обновлен!')
                return redirect('profile')
    else:
        form = ProfileEditForm(instance=user)

    return render(request, 'main/profile.html', {
        'form': form,
        'avatar_form': avatar_form
    })

@login_required
def profile_view(request):
    return render(request, 'main/profile.html')

def register_view(request):
    if request.method == 'POST':
        csrf_token = request.POST.get('csrfmiddlewaretoken')
        if not csrf_token:
            return HttpResponseForbidden("CSRF token missing")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'main/register.html', {'form': form})


@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'main/login.html', {'form': form})

def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def clinics(request):
    return render(request, 'main/clinics.html')


def moscow(request):
    return render(request, 'main/moscow.html')


def chita(request):
    return render(request, 'main/chita.html')


def samara(request):
    return render(request, 'main/samara.html')


def sochi(request):
    return render(request, 'main/sochi.html')

def services_list(request):
    categories = ServiceCategory.objects.prefetch_related(
        Prefetch('service_set',
                 queryset=Service.objects.filter(available=True).order_by('order'),
                 to_attr='available_services')
    ).filter(service__available=True).distinct()

    return render(request, 'main/services_list.html', {
        'categories': categories
    })

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, available=True)
    return render(request, 'main/service_detail.html', {'service': service})

