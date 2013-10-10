from django.db import models
from main.models import Producto

class Usuario(models.Model):
	uid = models.CharField(primary_key=True ,blank=False, max_length=60)
	username = models.CharField(unique=True, max_length=60)
	avatar = models.URLField()
	email = models.EmailField(blank=True, unique=True)
	backend = models.CharField(max_length=20)
	producto_votacion = models.ManyToManyField(Producto, related_name='vot+', through='Votacion')
	producto_compra = models.ManyToManyField(Producto ,through='Compra')

	def __unicode__(self):
		return self.username

class Compra(models.Model):
	usuario = models.ForeignKey(Usuario)
	producto = models.ForeignKey(Producto)
	fecha_compra = models.DateField(auto_now=True)

	class Meta:
		unique_together = ("usuario", "producto",)

class Votacion(models.Model):
	usuario = models.ForeignKey(Usuario)
	producto = models.ForeignKey(Producto)
	fecha_voto = models.DateField(auto_now=True)

	class Meta:
		unique_together = ("usuario", "producto",)

class Comentario(models.Model):
	usuario = models.ForeignKey(Usuario)
	producto = models.ForeignKey(Producto)
	comentario = models.CharField(max_length=140)
	fecha_comentario = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.comentario
