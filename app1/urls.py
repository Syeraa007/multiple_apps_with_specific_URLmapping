from django.urls import path
from app1.views import *

app_name='Application_1'

urlpatterns = [
    
    path('cool/', cool, name='cool'),
    path('hot/',hot,name='hot')

]