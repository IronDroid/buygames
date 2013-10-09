from django.contrib import admin
from .models import Usuario, Comentario, Compra, Votacion

class VotacionAdmin(admin.ModelAdmin):
	list_display = ('usuario', 'producto', 'fecha_voto',)
	
class UsuarioAdmin(admin.ModelAdmin):
	filter_horizontal = ('producto_votacion',)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Comentario)
admin.site.register(Compra)
admin.site.register(Votacion, VotacionAdmin)