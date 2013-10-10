from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404, get_list_or_404
from django.template import RequestContext
from .models import Producto, Screenshot
from usuarios.models import Usuario, Votacion, Compra
from inventario.models import Stock

def main(request):
	stocks = Stock.objects.all()
	productos = list()
	for stock in stocks:
		productos.append(stock.producto)
	if request.user.is_authenticated():
		usuario = Usuario.objects.get(uid=request.user.username)
		return render_to_response('home.html', {'productos':productos, 'usuario': usuario}, context_instance=RequestContext(request))
	else:
		return render_to_response('home.html', {'productos':productos}, context_instance=RequestContext(request))

def detail(request, idp):
	producto = get_object_or_404(Producto, pk=idp)
	capturas = Screenshot.objects.filter(id_producto = producto)
	votos = len(Votacion.objects.filter(producto=producto))
	if request.user.is_authenticated():
		usuario = Usuario.objects.get(uid=request.user.username)
		try:
			Compra.objects.get(usuario=usuario, producto=producto)
			is_compra = True
		except Compra.DoesNotExist:
			is_compra = False
		return render_to_response('detail.html', {
			'prod':producto, 'capturas':capturas, 'usuario':usuario, 'votos':votos, 'is_compra':is_compra}, context_instance=RequestContext(request))
	else:
		return render_to_response('detail.html', {
			'prod':producto, 'capturas':capturas, 'votos':votos}, context_instance=RequestContext(request))