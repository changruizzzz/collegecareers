from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Job


def index(request):
    jobs = Job.objects.all()
    return render(request, 'index.html', {'jobs': jobs})
