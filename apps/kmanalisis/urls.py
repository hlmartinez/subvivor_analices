from django.conf.urls import url
from django.urls import path , include
from apps.kmanalisis.views import variables,Upfile,csv_files_UP_list,deletecsv


#from apps.kmanalisis.views import dataAnalysis,tabla_vida_templete

urlpatterns = [
    path('variables/', variables, name="variables"),
    path('upfile/', Upfile, name="file"),
    path('upfile_list',csv_files_UP_list, name='csv_files_UP_list'),
    path('delete/<int:pk>', deletecsv, name="delete"),
]
