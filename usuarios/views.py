from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as social_logout

from django.contrib.auth.models import User
from social_auth.models import UserSocialAuth
from .models import Usuario, Compra
from main.models import Producto
from main.forms import UsuarioForm

@login_required
def perfil(request, user):
	usuario = Usuario.objects.get(uid=user)
	if request.method == 'POST':
		form = UsuarioForm(request.POST, instance=usuario)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = UsuarioForm(instance=usuario)
	return render_to_response('perfil.html', {'usuario':usuario}, context_instance=RequestContext(request, locals()))

@login_required
def logout(request):
	social_logout(request)
	return redirect('main')

@login_required
def delete(request, user):
	usuario = Usuario.objects.get(uid=user)
	if request.method == 'POST':
		print 'eliminar User'
		social_logout(request)
		u = User.objects.get(username = user)
		UserSocialAuth.objects.get(user = u).delete()
		u.delete()
		Usuario.objects.get(uid = user).delete()
		return HttpResponseRedirect('/')
	return render_to_response('delete.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required
def detalle_compra(request):
	usuario = Usuario.objects.get(uid=request.user)
	compras = Compra.objects.filter(usuario=usuario)
	listCompra = list()
	for c in compras:
		listCompra.append({'pk':c.pk, 'prod':Producto.objects.get(pk=c.producto.pk), 'fecha_compra':c.fecha_compra})

	return render_to_response('compras.html', {'usuario':usuario, 'compras':listCompra}, context_instance=RequestContext(request))