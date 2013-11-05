from django.db import models
from main.models import Producto
from usuarios.models import Usuario

# relacion
class Comentario(models.Model):
	user = models.ForeignKey(Usuario, related_name='user')
	prod = models.ForeignKey(Producto, related_name='prod')
	comment = models.TextField(max_length=140, unique=True)
	submit_date = models.DateTimeField(auto_now=True)