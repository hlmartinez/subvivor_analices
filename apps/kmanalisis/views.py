import json
import csv
import collections
from datetime import datetime
from django.db.models import Count
from django.http import Http404, HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
#from apps.kmanalisis.models import task_event, task_usage
from lifelines import KaplanMeierFitter
from django.core.files.storage import FileSystemStorage

from apps.kmanalisis.models import CSV
from apps.kmanalisis.forms import DocumentForm

filename = None
#kaplam - meier metodo de analisis de supervivencia
def get_kmf_fit(qs):
    duration = list(qs.values_list('dias_de_uso', flat=True))
    event_observed = list(qs.values_list('task_usage_vivo_muerto', flat=True))
    kmf = KaplanMeierFitter()
    kmf.fit(duration, event_observed)
    return kmf

def get_kmf_median(kmf):    
    return kmf.median_survival_time_

# obtener los grupos por prioridad
# def get_task_usage_by_cpu_uso(qs):
#     counts = {}
#     counts["task_usage_clasificacio_CPU_uso1"] = qs.filter(task_usage_clasificacio_CPU_uso = "0").count()
#     counts["task_usage_clasificacio_CPU_uso2"] = qs.filter(task_usage_clasificacio_CPU_uso = "1").count()
#     counts["task_usage_clasificacio_CPU_uso3"] = qs.filter(task_usage_clasificacio_CPU_uso = "2").count()
#     return counts


@login_required
def homeview(request):
    return render(request,'home.html')
    
#@method_decorator(login_required, name='dispatch')
@login_required
def Upfile(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.author = request.user
            # comment = form.save(commit=False)
            # comment.post = instance
            # comment.save()
            form.save()
            return  redirect('analisis:csv_files_UP_list')
    else:
        form = DocumentForm()
    return render(request, 'upfile.html',{'form' :form})


@login_required
def csv_files_UP_list(request):
    csvs = CSV.objects.all()
    return render(request,'upfilelist.html',{'csvs' :csvs})


def deletecsv(request,pk):
    if request.method == 'POSR':
        csvs = CSV.objects.get(pk=pk)
        csvs.delete()
    return redirect('analisis:csv_files_UP_list')    



def variables(request):
    print(filename)
    return render(request,'variables.html')

    



# Create your views here.
# class dataAnalysis(TemplateView): 
#     #template_name = "index.html"
#     def index(request):
#         task_events = task_event.objects.all()
#         task_usages = task_usage.objects.all()
#         #print(task_usages)
#         #separando los vivos y muertos
#         vivos_cases = task_usages.filter(task_usage_vivo_muerto="0")
#         muertos_cases = task_usages.filter(task_usage_vivo_muerto="1")
#         # valores total y total por clasificacion de uso del cpu
#         total_count = task_usages.all().count()
#         total_by_cpu = get_task_usage_by_cpu_uso(task_usages)
#         # cantidad de casos por contadores en los casos de vida
#         vivos_cases_count = vivos_cases.count()
#         open_by_cpu = get_task_usage_by_cpu_uso(vivos_cases)
#         kmf_fit = get_kmf_fit(task_usages)
#         var = kmf_fit.plot()
#         median_wait_time_kmf = get_kmf_median(kmf_fit)
#         print (vivos_cases_count)
#         print (median_wait_time_kmf)
#         print (vivos_cases_count)
#         context = {
#             "casoso_vivos" : vivos_cases_count,
#             "analisis_result" : kmf_fit,
#             "grafico" : var
#         }

    
#         return render(request, "login.html", context) 



# class tabla_vida_templete(TemplateView):
#     def tabla_vida(request):
#         return render(request, "tabla_vida.html", {})