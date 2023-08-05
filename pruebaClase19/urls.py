
from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),

    #apunta a la urls de la aplicacion
    path('', include('app1.urls')),
]
