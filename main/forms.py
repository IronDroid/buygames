#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.contrib.comments import Comment
from usuarios.models import Usuario
from tendencia.models import Comentario

class UsuarioForm(ModelForm):
	username = forms.CharField(
		label='',
		widget=forms.TextInput(attrs={
			'class':'form-control',
            'placeholder':'Nombre de Usuario'}))
	email = forms.CharField(
		label='',
		widget=forms.TextInput(attrs={
			'class':'form-control',
            'placeholder':'Correo electronico'}))
	nro_tarjeta = forms.IntegerField(
		label='',
		widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Numero de Tarjeta'})
	)
	cvc = forms.IntegerField(
		label='',
		widget=forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'CVC'
			}))
	mes_vencimiento = forms.IntegerField(
		label='',
		widget=forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'Mes de Vencimiento'
			}))
	year_vencimiento = forms.IntegerField(
		label='',
		widget=forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'Año de Vencimiento'
			}))
	class Meta:
		model = Usuario
		exclude = ('uid', 'avatar','backend', 'producto_votacion', 'producto_compra',)

class ComentarioForm(ModelForm):
	comment = forms.CharField(widget=forms.Textarea, label='', max_length=140)
	class Meta:
		model = Comentario
		exclude = ('user', 'prod', 'submit_date',)