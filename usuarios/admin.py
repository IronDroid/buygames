from django.contrib import admin
from .models import Usuario, Compra, Votacion

class VotacionAdmin(admin.ModelAdmin):
	list_display = ('usuario', 'producto', 'fecha_voto',)
	
class UsuarioAdmin(admin.ModelAdmin):
	filter_horizontal = ('producto_votacion',)

class CompraAdmin(admin.ModelAdmin):
	list_display = ('usuario', 'producto',)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Votacion, VotacionAdmin)