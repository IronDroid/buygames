from django.db import models

class Plataforma(models.Model):
	descripcion_plat = models.TextField(max_length=50)

	def __unicode__(self):
		return self.descripcion_plat

class Genero(models.Model):
	descripcion_genero = models.TextField(max_length=50)

	def __unicode__(self):
		return self.descripcion_genero
# tiene 2 ralaciones
class Producto(models.Model):
	nombre = models.CharField(max_length=140)
	portada = models.ImageField(upload_to='portada')
	descripcion = models.CharField(max_length=140)
	fecha_lanzamiento = models.DateField()
	trailer = models.URLField()
	plataforma = models.ManyToManyField(Plataforma)
	genero = models.ForeignKey(Genero)
	precio = models.FloatField()

	def __unicode__(self):
		return self.nombre

# tiene relacion
class Screenshot(models.Model):
	id_producto = models.ForeignKey(Producto)
	img_captura = models.ImageField(upload_to='imagenes')

	def __unicode__(self):
		return self.img_captura