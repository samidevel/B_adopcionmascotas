from django.urls import path
from apps.adopcion.views import index_adopcion


#urlpatterns = [
    #path('/', index),
#]

app_name = 'adopcion'
urlpatterns = [
    path('index', index_adopcion),
]