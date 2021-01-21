from django.db import models
from datetime import datetime
from django.db.models import Avg
from django.utils import dateformat
from lifelines import KaplanMeierFitter
from django.conf import settings
import csv
import json
import logging



logger = logging.getLogger(__name__)

print ("entre en el model")
#kaplam - meier metodo de analisis de supervivencia
def get_kmf_fit(qs,valorLista,evento):
    t = qs.values_list(valorLista, flat=True)
    c = qs.values_list(evento, flat=True)
    kmf = KaplanMeierFitter()
    kmf.fit(t, event_observed=c)
    return kmf

def get_kmf_median(kmf):    
    return kmf.median_


# class task_event(models.Model):
#     task_events_time=models.BigIntegerField()
#     task_events_missing_info=models.BigIntegerField(blank=True, null=True)
#     task_events_job_id=models.BigIntegerField()
#     task_events_index=models.BigIntegerField(db_index=True)
#     task_events_machine_id=models.BigIntegerField(blank=True,null=True)
#     task_events_event_type=models.BigIntegerField()
#     task_events_user=models.TextField(max_length=200,blank=True,null=True)
#     task_events_scheduling_class=models.BigIntegerField(blank=True, null=True)
#     task_events_priority=models.IntegerField()
#     task_events_CPU_request=models.FloatField(blank=True, null=True)
#     task_events_memory_request=models.FloatField(blank=True, null=True)
#     task_events_disk_space_request=models.FloatField(blank=True, null=True)
#     task_events_machine_restriction=models.BooleanField(blank=True, null=True)

#     # Managers
#     objects = models.Manager()

#     class Meta:
#         ordering = ("-task_events_machine_id",)

#     #def __unicode__(self):
#         #return unicode(self.csr)

#     def __str__(self):
#         return self.task_events_machine_id
#         #return f"{self.task_events_time} {self.task_events_missing_info} {self.task_events_job_id} {self.task_events_index} {self.task_events_machine_id} {self.task_events_event_type} {self.task_events_user} {self.task_events_scheduling_class} {self.task_events_priority} {self.task_events_CPU_request} {self.task_events_memory_request} {self.task_events_disk_space_request} {self.task_events_machine_restriction}"


# class task_usage(models.Model):
#     task_usage_start_time=models.DateField()
#     task_usage_end_time=models.DateField(blank=True,null=True)
#     task_usage_job_id=models.BigIntegerField()
#     task_usage_tanks_index=models.BigIntegerField(db_index=True)
#     task_usage_machine_id=models.BigIntegerField()
#     task_usage_CPU_rate=models.FloatField(blank=True,null=True)
#     task_usage_canonical_usage_memory=models.FloatField(blank=True,null=True)
#     task_usage_assigned_usage_memory=models.FloatField(blank=True,null=True)
#     task_usage_unmapped_page_cache=models.FloatField(blank=True,null=True)
#     task_usage_total_page_cache=models.FloatField(blank=True,null=True)
#     task_usage_maximum_usage_memory=models.FloatField(blank=True,null=True)
#     task_usage_disk_time=models.FloatField(blank=True,null=True)
#     task_usage_local_disk_space=models.FloatField(blank=True,null=True)
#     task_usage_max_CPU_rate=models.FloatField(blank=True,null=True)
#     task_usage_max_disk_time=models.FloatField(blank=True,null=True)
#     task_usage_cicles_x_instuction=models.FloatField(blank=True,null=True)
#     task_usage_memory_accesses_x_instruction=models.FloatField(blank=True,null=True)
#     task_usage_simple_partition=models.FloatField(blank=True,null=True)
#     task_usage_agregation_type=models.BooleanField(blank=True,null=True)
#     task_usage_sampled_CPU_usage=models.FloatField(blank=True,null=True)
#     #propios
#     task_usage_clasificacio_CPU_uso = models.IntegerField()
#     task_usage_vivo_muerto = models.BooleanField()
#     #task_usage_tiempo_vida = models.CharField(max_length=250)
#     gt_30_days = models.BooleanField(default=False, verbose_name="Older than 30 days")
#     gt_90_days = models.BooleanField(default=False, verbose_name="Older than 90 days")
#     gt_180_days = models.BooleanField(default=False, verbose_name="Older than 180 days")
#     mas_de_un_anno = models.BooleanField(default=False, verbose_name="Older than one year")
#     dias_de_uso = models.IntegerField(null=True)
    

#     objects = models.Manager()

#     def __str__(self):
#         #return f"{self.task_usage_start_time} {self.task_usage_end_time} {self.task_usage_job_id} {self.task_usage_tanks_index} {self.task_usage_machine_id} {self.task_usage_CPU_rate} {self.task_usage_start_time} {self.task_usage_canonical_usage_memory} {self.task_usage_assigned_usage_memory} {self.task_usage_start_time} {self.task_usage_start_time} {self.task_usage_unmapped_page_cache} {self.task_usage_maximum_usage_memory} {self.task_usage_disk_time} {self.task_usage_local_disk_space} {self.task_usage_max_CPU_rate} {self.task_usage_max_disk_time} {self.task_usage_cicles_x_instuction} {self.task_usage_memory_accesses_x_instruction} {self.task_usage_simple_partition} {self.task_usage_agregation_type} {self.task_usage_sampled_CPU_usage} {self.task_usage_total_time} {self.task_usage_clasificacio_CPU_uso} {self.task_usage_vivo_muerto} {self.task_usage_tiempo_vida}"
#         return self.task_usage_machine_id
#     class Meta:
#         ordering = ("-task_usage_machine_id",)
 
# #Calculando el tiepo de la interrupcion en task_usage
#     def get_tiempo_de_uso(self):
#         t = self.task_usage_start_time - self.task_usage_end_time 
#         #falta convertir este dato
#         return t
# #Obtener v o f en caso de que lso tiempos de uso en sean menores que una variable entrada ejemplo para saber 
# # si la interrucion estuvo presente por determinado tiempo 
    
#     def get_comparacion_uso_RAM(self,n):
#         if self.task_usage_maximum_usage_memory > n:
#             return True
#         return False
    
#     def get_comparacion_uso_CPU(self,n):
#         if self.task_usage_sampled_CPU_usage > n:
#             return True
#         return False
    
# en este model de guardara la informacion de los analis de cada usuario
class Previo(models.Model):
    usuarios = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #datos analisis
    cant_entrada = models.BigIntegerField()
    cant_sensured = models.BigIntegerField()
    media = models.FloatField()
    #metadatos del analisis y covariables
   
    class Meta:
       verbose_name = 'Previo'
       verbose_name_plural = 'Previos'
       ordering  = ['usuarios']

    def __str__(self):
        return self.usuarios
    


def gatuser_name_folder(intancia, filename):
    return 'user_{0}/{1}'.format(intancia.user.id,filename)
class CSV(models.Model):
    usercsv = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='documents')
    file = models.FileField(upload_to='files')
    cargado_en = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.usercsv
    
    objects = models.Manager()
    
    # def delete(self,*args, **kwargs):
    #     self.file.delete()
    #     super().delete(*args, **kwargs)
