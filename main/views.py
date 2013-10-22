from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404, get_list_or_404
from django.template import RequestContext
from .models import Producto, Screenshot, Plataforma, Genero
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
			'prod':producto, 'capturas':capturas, 'usuario':usuario, 'votos':votos, 'is_compra':is_compra}, context_instance=RequestContext(request, locals()))
	else:
		return render_to_response('detail.html', {
			'prod':producto, 'capturas':capturas, 'votos':votos}, context_instance=RequestContext(request, locals()))

def plataforma(request):
	stocks = Stock.objects.all()
	plat = Plataforma.objects.all()
	platlist = list()
	platdict = dict()
	for p in plat:
		platdict = dict()
		productos = list()
		platdict['plat'] = p.descripcion_plat
		for stock in stocks:
			for descplat in stock.producto.plataforma.values():
				if descplat['descripcion_plat'] == p.descripcion_plat:
					productos.append(stock.producto)
		else:
			platdict['prod'] = productos
		platlist.append(platdict)

	if request.user.is_authenticated():
		usuario = Usuario.objects.get(uid=request.user.username)
		return render_to_response('plataforma.html', {'platdict':platlist, 'usuario': usuario}, context_instance=RequestContext(request))
	else:
		return render_to_response('plataforma.html', {'platdict':platlist}, context_instance=RequestContext(request))

def genero(request):
	stocks = Stock.objects.all()
	gen = Genero.objects.all()
	genlist = list()
	gendict = dict()
	for g in gen:
		gendict = dict()
		productos = list()
		gendict['gen'] = g.descripcion_genero
		for stock in stocks:
			print '*' *15
			if stock.producto.genero == g:
				print True
				productos.append(stock.producto)
			print '*' *15
		else:
			gendict['prod'] = productos
		genlist.append(gendict)

	print genlist

	if request.user.is_authenticated():
		usuario = Usuario.objects.get(uid=request.user.username)
		return render_to_response('genero.html', {'gendict':genlist, 'usuario': usuario}, context_instance=RequestContext(request))
	else:
		return render_to_response('genero.html', {'gendict':genlist}, context_instance=RequestContext(request))