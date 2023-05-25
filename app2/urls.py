from django.urls import path
from app2.views import *

app_name='Application_2'

urlpatterns = [
    
    path('simha/', simha, name='simha'),
    path('reddy/',reddy,name='reddy')

]