from django import forms
from django.forms import ModelForm
from django.contrib.comments import Comment
from usuarios.models import Usuario
from tendencia.models import Comentario

class UsuarioForm(ModelForm):
	class Meta:
		model = Usuario
		exclude = ('uid', 'avatar','backend', 'producto_votacion', 'producto_compra',)

class ComentarioForm(ModelForm):
	comment = forms.CharField(widget=forms.Textarea, label='', max_length=140)
	class Meta:
		model = Comentario
		exclude = ('user', 'prod', 'submit_date',)