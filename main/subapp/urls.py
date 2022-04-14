from django.urls import path
from subapp.views import csv_file
from django.views.decorators.csrf import csrf_exempt
 
urlpatterns = [
    path('csv/', csrf_exempt(csv_file),name='csv-file')
]
