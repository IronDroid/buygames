from django.contrib import admin
from .models import Comentario

class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('user', 'prod', 'comment', 'submit_date',)

admin.site.register(Comentario, ComentarioAdmin)