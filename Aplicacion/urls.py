from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    
    
    path('home',views.Home,name="Home"),
    path('servicios',views.servicios, name="Servicios"),
    path('tienda',views.tienda, name="Tienda"),
    path('registrate',views.registrate, name="Registrate"),
    path('Bas',views.Bas, name="Bas"),
    path('funcion', views.funcion,name='funcion'),
    path('ferreteria', views.ferreteria,name='ferreteria'),
    path('crear', views.crear,name='crear'),
    path('eliminar<int:id>', views.eliminar,name='eliminar'),
    path('editar<int:id>', views.editar,name='editar'),
    path('index', views.index,name='index'),
    path('header', views.header,name='header'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

