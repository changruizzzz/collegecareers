from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.models import User


def signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return render(request, 'users/signform.html', {'login': True})


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return render(request, 'users/signform.html', {'signup': True})


@login_required(login_url='/signin/')
def settings(request):
    return render(request, 'users/settings.html', {})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(email=email, password=password)
    if not user:
        user = authenticate(username=email, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return JsonResponse({'message': 'success'})
        else:
            return JsonResponse({'message': 'inactive'})
    else:
        return JsonResponse({'message': 'invalid'})


def signup_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = User.objects.create_user(email, password)
        user.save()
        login(request, user)
    except IntegrityError:
        return JsonResponse({'message': 'invalid'})
    return JsonResponse({'message': 'success'})
