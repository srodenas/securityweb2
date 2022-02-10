from django.contrib import admin
from .models import *

# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','email')
    search_fields = ['nombre']
    
class ArticuloAdmin(admin.ModelAdmin):
    list_display=('descripcion',)
    search_fields = ['descripcion']
    

#admin.site.register(Cliente)
#admin.site.register(Articulo)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Articulo, ArticuloAdmin)
