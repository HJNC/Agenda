from django.contrib import admin
from core.models import Evento
# Register your models here.

class EventoAdmin(admin.ModelAdmin):

    #cabeçalho
    list_display = ('id','titulo','data_evento', 'data_criacao')

    #filtro
    list_filter = ('usuario','data_evento')

#Associa na pagina
admin.site.register(Evento, EventoAdmin)
