from django.contrib import admin
from .models import newuser,bien,status,client,contrat,tests,prestations, personnel,modereglement
from . import models
 
# Register your models here.
admin.site.register(newuser,)
admin.site.register(status,)
admin.site.register(client,)
admin.site.register(contrat,)
admin.site.register(tests,)
admin.site.register(prestations,)
admin.site.register(personnel,)
admin.site.register(modereglement,)







@admin.register(models.bien)
class bien(admin.ModelAdmin):
    list_display=('id','nom') #Ordre d'affichage
    ordering=('id','nom') #Ordonner par ID
    list_filter=('id','nom')     #Filtrer
    search_fields=('id','nom')     #Actier la zone de recherche


