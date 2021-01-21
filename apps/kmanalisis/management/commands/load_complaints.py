import csv
import random
import pandas as pd
import datetime
import logging
import os   
from django.conf import settings
from ast import literal_eval as make_tuple
from django.core.management.base import BaseCommand, CommandError
from apps.kmanalisis.models import task_event, task_usage
from random import randrange, choice
from apps.kmanalisis.datos.obtener_path import getPath

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def clasificacio_CPU_uso(self, valor):
        if float(valor) <= 2.0:
            return 0
        elif  float(valor) <= 4.0:
            return 1
        else:
            return 2

    def vivo_muerto(self):
        return int(random.randrange(0,2,step=1,_int=int))

    def parse_fecha_inicio(self, miliseg):
        dia = random.randrange(1,29,step=1,_int=int)
        mes = random.randrange(1,12,step=1,_int=int)
        anno = random.randrange(2011,2017,step=1,_int=int) 
        base_datetime = datetime.datetime( anno, mes, dia )
        delta = datetime.timedelta( 0, 0, int(miliseg), 0)
        dateini = base_datetime + delta
        return dateini
        
    def parse_fecha_fin(self, miliseg,timeinicio,vivomuerto):
        if vivomuerto:
            tiempo_vida_aleatorio_dias= random.randrange(1,600,step=1,_int=int)
            delta = datetime.timedelta( tiempo_vida_aleatorio_dias, 0, int(miliseg) ,0  )
            dateini = timeinicio + delta
            return dateini
        else:
            pass

    def flush_usage(self):
        task_usage.objects.all().delete()
        task_event.objects.all().delete()

    def parse_valoresvacios(self,valor):
        if valor == '': 
            valor = None
        return valor

    def get_dias_de_uso(self,vivo_muerto,fechainicio,fechafin):
        fecha_reciente = datetime.datetime.now()
        if vivo_muerto:
            t = fechafin - fechainicio
        else:
            t = fecha_reciente - fechainicio
        return t.days

    def get_gt_t_days(self, n,dias_de_uso):
        if dias_de_uso > n:
            return True
        return False


    def handle(self, *args, **options):
        self.data_dir = os.path.join(settings.BASE_DIR, 'apps\kmanalisis', 'datos')
        logger.debug("flushing usage")
        #clean database
        #self.flush_usage()
        task_event_list = []
        task_usage_list = []
        pathsevent = ['event_part-00001-of-00500.csv']
        pathsusage = ['usage_part-00000-of-00500.csv']
        print("Lectura de archivos completada")
        
        for p in pathsevent:
            path = os.path.join(self.data_dir, p)
            reader = csv.DictReader(open(path, 'r'))
            print("Cargando datos en taks_event")
            contador = 0
            for row in reader:
                c = task_event(
                    task_events_time = row["task_events_time"],
                    task_events_missing_info = self.parse_valoresvacios(row["task_events_missing_info"]),
                    task_events_job_id = row["task_events_job_id"],
                    task_events_index = row["task_events_index"],
                    task_events_machine_id = self.parse_valoresvacios(row["task_events_machine_id"]),
                    task_events_event_type = row["task_events_event_type"],
                    task_events_user = row["task_events_user"],
                    task_events_scheduling_class = int(row["task_events_scheduling_class"]),
                    task_events_priority = row["task_events_priority"],
                    task_events_CPU_request = row["task_events_CPU_request"],
                    task_events_memory_request = row["task_events_memory_request"],
                    task_events_disk_space_request = row["task_events_disk_space_request"],
                    task_events_machine_restriction = row["task_events_machine_restriction"],
                    ) 
                #print(c)
                c.save()
                
                #task_event_list.append(c)

        print("Fin de carga de valores de tanks_event")

        # Batch upload to the database, 500 at a time
        #task_events.objects.bulk_create(
           # task_event_list,
           # batch_size=500
        #)#

        for u in pathsusage:
            path = os.path.join(self.data_dir, u)
            reader = csv.DictReader(open(path, 'r'))
            print("Pasando a la tablas de tanks_usage")
            contador = 0
            for row in reader:
                vivomuerto = self.vivo_muerto()
                timeinicio = self.parse_fecha_inicio(row["task_usage_start_time"])
                timefin = self.parse_fecha_fin(row["task_usage_end_time"],timeinicio,vivomuerto)
                dias = self.get_dias_de_uso(vivomuerto,timeinicio,timefin)
                x = task_usage(
                    task_usage_start_time = timeinicio,
                    task_usage_end_time = timefin,
                    task_usage_job_id = row["task_usage_job_id"],
                    task_usage_tanks_index = row["task_usage_tanks_index"],
                    task_usage_machine_id = row["task_usage_machine_id"],
                    task_usage_CPU_rate = self.parse_valoresvacios(row["task_usage_CPU_rate"]),
                    task_usage_canonical_usage_memory = self.parse_valoresvacios(row["task_usage_canonical_usage_memory"]),
                    task_usage_assigned_usage_memory = self.parse_valoresvacios(row["task_usage_assigned_usage_memory"]),
                    task_usage_unmapped_page_cache = self.parse_valoresvacios(row["task_usage_unmapped_page_cache"]),
                    task_usage_maximum_usage_memory = self.parse_valoresvacios(row["task_usage_maximum_usage_memory"]),
                    task_usage_disk_time = self.parse_valoresvacios(row["task_usage_disk_time"]),
                    task_usage_local_disk_space = self.parse_valoresvacios(row["task_usage_local_disk_space"]),
                    task_usage_max_CPU_rate = self.parse_valoresvacios(row["task_usage_max_CPU_rate"]),
                    task_usage_max_disk_time = self.parse_valoresvacios(row["task_usage_max_disk_time"]),
                    task_usage_cicles_x_instuction = self.parse_valoresvacios(row["task_usage_cicles_x_instuction"]),
                    task_usage_memory_accesses_x_instruction = self.parse_valoresvacios(row["task_usage_memory_accesses_x_instruction"]),
                    task_usage_simple_partition = self.parse_valoresvacios(row["task_usage_simple_partition"]),
                    task_usage_agregation_type = self.parse_valoresvacios(row["task_usage_agregation_type"]),
                    task_usage_sampled_CPU_usage = self.parse_valoresvacios(row["task_usage_sampled_CPU_usage"])
                    )
                #propiostask_usage_start_time          
                x.task_usage_clasificacio_CPU_uso = self.clasificacio_CPU_uso(x.task_usage_max_CPU_rate)
                x.task_usage_vivo_muerto = vivomuerto
                x.gt_30_days = self.get_gt_t_days(30,dias)
                x.gt_90_days = self.get_gt_t_days(90,dias)
                x.gt_180_days = self.get_gt_t_days(180,dias)
                x.mas_de_un_anno = self.get_gt_t_days(365,dias)
                x.dias_de_uso = dias 
                #task_usage_list.append(x)
                #print(x)
                x.save()


        logger.debug("Loading complaints to database.")
        print("Fin de carga de valores de tanks_usage")

        # Batch upload to the database, 500 at a time
        task_usage.objects.bulk_create(
            task_usage_list,
            batch_size=500
        )

