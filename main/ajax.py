from django.shortcuts import get_list_or_404
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from main.models import Producto
from usuarios.models import Votacion, Usuario, Compra
from inventario.models import Stock

@dajaxice_register
def sayhello(request, pid):
	user = Usuario.objects.get(uid=request.user)
	prod = Producto.objects.get(pk=pid)
	voto, created = Votacion.objects.get_or_create(usuario=user, producto=prod)
	if not created:
		voto.delete()
	cant = len(Votacion.objects.filter(producto=prod))
	return simplejson.dumps({'cant':cant})

@dajaxice_register
def comprar(request, pid):
	user = Usuario.objects.get(uid=request.user)
	prod = Producto.objects.get(pk=pid)
	s = Stock.objects.get(producto=prod)
	print s.stock
	created = False
	if s.stock == 0:
		stock = False;
	if s.stock > 0:
		stock = True;
		compra, created = Compra.objects.get_or_create(usuario=user, producto=prod)
		if created:
			s.stock = s.stock - 1
			s.save()
		print created
	print stock
	return simplejson.dumps({'compra':created, 'stock':stock})