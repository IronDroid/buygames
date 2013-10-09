from django.db import models
from main.models import Producto

class Empresa(models.Model):
	nombre = models.TextField(max_length=40)
	webpage = models.URLField()
	producto_licencias = models.ManyToManyField(Producto, through='Stock')

	def __unicode__(self):
		return self.nombre

class Stock(models.Model):
	empresa = models.ForeignKey(Empresa)
	producto = models.ForeignKey(Producto)
	stock = models.IntegerField()

	class Meta:
		unique_together = ('producto',)