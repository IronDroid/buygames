from django import forms
from django.forms import ModelForm
from django.contrib.comments import Comment
from usuarios.models import Usuario

class UsuarioForm(ModelForm):
	class Meta:
		model = Usuario
		exclude = ('uid', 'avatar','backend', 'producto_votacion', 'producto_compra',)
