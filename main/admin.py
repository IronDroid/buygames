from django.contrib import admin
from .models import Producto, Plataforma, Genero, Screenshot

class ScreenshotAdmin(admin.ModelAdmin):
	list_display = ('img_captura',)

class ScreenshotInline(admin.StackedInline):
	model = Screenshot
	extra = 2

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'fecha_lanzamiento', 'genero',)
	inlines = [ScreenshotInline]
	filter_horizontal = ('plataforma',)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Plataforma)
admin.site.register(Genero)
admin.site.register(Screenshot, ScreenshotAdmin)
