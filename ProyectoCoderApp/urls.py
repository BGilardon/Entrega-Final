from django.urls import path

from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # URLS de ProyectoCoderApp
    path('', campo, name="campo"),
    path('login', login_request, name="login"), # no usar login como nombre de la vista
    path('register', register_request, name="register"),
    path('logout', logout_request, name="logout"),
    
    path('posteos', posteos, name="posteos"),
    path('crearPosteos/' , crearPosteos , name = "crearPosteos"),

    path(r'^editar/(?P<pk>\d+)$', PosteoUpdate.as_view(), name="posteo_update"),
    path(r'^eliminar/(?P<pk>\d+)$', PosteoDelete.as_view(), name="posteo_delete"),


    # path('base/', base),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
