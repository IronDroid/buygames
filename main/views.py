from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from .forms import ComentarioForm
from .models import Producto, Screenshot, Plataforma, Genero
from usuarios.models import Usuario, Votacion, Compra
from inventario.models import Stock
from tendencia.models import Comentario

def main(request):
	stocks = Stock.objects.all()
	productos = list()
	for stock in stocks:
		productos.append(stock.producto)

	dict_return = dict()
	if request.user.is_authenticated():
		usuario = Usuario.objects.get(uid=request.user.username)
		dict_return = {'productos':productos, 'usuario': usuario}
	else:
		dict_return = {'productos':productos}
	
	return render_to_response('home.html', dict_return, context_instance=RequestContext(request))

def detail(request, idp):
	producto = get_object_or_404(Producto, pk=idp)
	capturas = Screenshot.objects.filter(id_producto = producto)
	votos = len(Votacion.objects.filter(producto=producto))
	comentarios = Comentario.objects.order_by("-submit_date").filter(prod=producto)

	dict_return = dict()
	if request.user.is_authenticated():
		usuario = Usuario.objects.get(uid=request.user.username)
		comment = Comentario(user=usuario, prod=producto)
		if request.method == 'POST':
			form = ComentarioForm(request.POST, instance=comment)
			if form.is_valid():
				form.save()
				return redirect('detail', idp)
		else:
			form = ComentarioForm(instance=comment)

		try:
			Compra.objects.get(usuario=usuario, producto=producto)
			is_compra = True
		except Compra.DoesNotExist:
			is_compra = False

		dict_return = {'prod':producto, 'capturas':capturas, 'usuario':usuario, 'votos':votos, 'is_compra':is_compra, 'comments':comentarios}
	else:
		dict_return = {'prod':producto, 'capturas':capturas, 'votos':votos, 'comments':comentarios}
	
	return render_to_response('detail.html', dict_return, context_instance=RequestContext(request, locals()))

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

	dict_return = dict()
	if request.user.is_authenticated():
		usuario = Usuario.objects.get(uid=request.user.username)
		dict_return =  {'platdict':platlist, 'usuario': usuario}
	else:
		dict_return = {'platdict':platlist}

	return render_to_response('plataforma.html', dict_return, context_instance=RequestContext(request))

def genero(request):
	stocks = Stock.objects.all()
	gen = Genero.objects.all()
	genlist = list()
	gendict = dict()
	for g in gen:
		gendict = dict()
		productos = list()
		for stock in stocks:
			if stock.producto.genero == g:
				productos.append(stock.producto)
		else:
			if len(productos) > 0:
				gendict['gen'] = g.descripcion_genero
				gendict['prod'] = productos
				genlist.append(gendict)
	dict_return = dict()
	if request.user.is_authenticated():
		usuario = Usuario.objects.get(uid=request.user.username)
		dict_return = {'gendict':genlist, 'usuario': usuario}
	else:
		dict_return = {'gendict':genlist}
	return render_to_response('genero.html', dict_return, context_instance=RequestContext(request))