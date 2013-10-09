from django.contrib import admin
from .models import Empresa, Stock

class EmpresaAdmin(admin.ModelAdmin):
	list_display = ('nombre','webpage',)

class StockAdmin(admin.ModelAdmin):
	list_display = ('empresa','producto','stock',)

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Stock, StockAdmin)