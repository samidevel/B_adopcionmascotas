from django.urls import path
from apps.mascota.views import index

#urlpatterns = [
    #path('/', index),
#]
#app_name = 'mascota'

#app_name = "mascota"
urlpatterns = [
    path('', index),
]