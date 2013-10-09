from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as social_logout

from django.contrib.auth.models import User
from social_auth.models import UserSocialAuth
from .models import Usuario

@login_required
def perfil(request, user):
	usuario = Usuario.objects.get(uid=user)
	return render_to_response('perfil.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required
def logout(request):
	social_logout(request)
	return redirect('main')

@login_required
def delete(request, uid):
	print '*' * 35
	# social_logout(request)
	# User.objects.get(username=uid).delete()
	# UserSocialAuth.objects.get(user=User.objects.get(username=uid)).delete()
	# Usuario.objects.get(uid=uid).delete()
	return redirect('main')