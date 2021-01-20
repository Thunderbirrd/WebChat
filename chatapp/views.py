from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from authapp.models import User
from django.http import HttpResponse


@login_required(login_url='/auth/login/')
def search_user(request):
    username = json.load(request)['username']
    user = User.objects.get(username=username)
    if user:
        pass
    else:
        return HttpResponse("No such user")
    return None
