
from django.contrib import admin
from django.urls import path,include
from sigim.views import adreglementm,espacefacturem,adfactm,etatprofm,supligneprof,apidetailsprof,detailprofm,espaceproform,adprofm,createTest,apiprestation,apicompbien,adproformabail,adprofmanda,proformamandat,proformabail,modifproprio,load_piece_details,propsectproprio,espacepersonnel,prospectcontrat,espacecontrat,test,sample_data,load_piece,adcontrat,modifclient,prospectclient,espaceclient,adclient,maquette,test,home,conex,aduser,adypepiece,espaceadmin,espacestaff,espacebien,espaceproprio,adproprio,adbien,adcompbien,prospectbien,espacecompobien,modifbien
#POUR LA GESTION DES FICHIERS STATIC: IMAGE, VIDEOS
from django.conf.urls.static import static
from django.conf import settings
from sigim import views
from sigim.api import compbienviewset, contratserializer
from rest_framework.routers import DefaultRouter 

#Creation d'API avec rest_framework
router=DefaultRouter()
router.register(r'compbien',compbienviewset,basename='compbien')



urlpatterns = [
    #path('', include(router.urls)),
    path('compbien', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) ,   
    path('test',test, name='test'),
    path('maquette',maquette, name='maquette'),
    path('',home,name='home'),
    path('conex',conex,name='conex'),
    path('admin/', admin.site.urls),

    #DETAILS
    path('detailprofm/<int:idprof>',detailprofm, name='detailprofm'),


    #PROSPECTS
    path('prospectbien',prospectbien, name='prospectbien'),
    path('propsectproprio', propsectproprio, name='propsectproprio'),
    path('prospectclient',prospectclient, name='prospectclient'),
    path('prospectcontrat', prospectcontrat, name='prospectcontrat'),


    #ESPACES
    path('espaceadmin',espaceadmin,name='espaceadmin'),
    path('espacestaff',espacestaff,name='espacestaff'),
    path('espacebien',espacebien,name='espacebien'),
    path('espacecompobien/<int:id>',espacecompobien, name='espacecompobien'),
    path('espaceproprio',espaceproprio, name='espaceproprio'),
    path('espacecontrat', espacecontrat, name='espacecontrat'),
    path('espacepersonnel', espacepersonnel, name='espacepersonnel'),
    path('espaceproform', espaceproform, name='espaceproform'),
    path('espaceclient',espaceclient, name='espaceclient'),
    path('proformamandat', proformamandat, name='proformamandat'),
    path('proformabail', proformabail, name='proformabail'),
    path('espacefacturem', espacefacturem, name='espacefacturem'),

    #AJOUT
    path('aduser',aduser,name='aduser'),
    path('adprofmanda/<int:id>', adprofmanda, name='adprofmanda'),
    path('adproformabail/<int:id>', adproformabail, name='adproformabail'),
    path('adprofm/<int:idproprietaire>',adprofm, name='adprofm'),
    path('adypepiece',adypepiece,name='adypepiece'),
    path('adbien',adbien,name='adbien'),
    path('adcompbien/<int:id>',adcompbien, name='adcompbien'),
    path('adproprio',adproprio, name='adproprio'),
    path('adclient',adclient,name='adclient'),
    path('adcontrat',adcontrat, name='adcontrat'),
    path('createTest/',createTest,name='createTest') , 
    path('adfactm/<int:idprof>', adfactm , name='adfactm'),
    path('adreglementm/<int:idfac>', adreglementm , name='adreglementm'),

    #MODIFICATION
    path('modifclient/<int:id>',modifclient, name='modifclient'),
    path('modifbien/<int:id>',modifbien, name='modifbien'),
    path('modifproprio/<int:id>',modifproprio, name='modifproprio'),

    #SUPPRESSION
    
    path('supligneprof/<int:idligne>', supligneprof, name='supligneprof'),


    #API
    path('apidetailsprof', apidetailsprof, name='apidetailsprof'),
    path('sample_data/',sample_data, name='sample_data'),
    path('load_piece/',load_piece, name='load_piece'),
    path('load_piece_details/', load_piece_details, name='load_piece_details'),
    path('apiprestation', apiprestation, name='apiprestation'),


    #ETAT
    path('etatprofm/<int:idprof>', etatprofm, name='etatprofm'),
    path('etatprofm', views.etatprofm, name='etatprofm'),

    #RECUP COORDONNEES GPS
    path('envoyer_coordonnees', views.envoyer_coordonnees, name='envoyer_coordonnees'),



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



#RECUPERATION DES FICHIERS STATIC
#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL,
    #document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)