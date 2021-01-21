from django.contrib import admin
from apps.kmanalisis.models import Previo,CSV

# Register your models here.
# print("entre en el admin")
# class task_events_Admin(admin.ModelAdmin):
#     list_display = ["task_events_time" , "task_events_missing_info" , "task_events_job_id" , "task_events_index" , "task_events_machine_id" , "task_events_event_type" , "task_events_user" , "task_events_scheduling_class" , "task_events_priority" , "task_events_CPU_request" , "task_events_memory_request"  , "task_events_disk_space_request" , "task_events_machine_restriction"]
    
#     class Meta:
#         model = task_event

# class task_usage_Admin(admin.ModelAdmin):
#     list_display = ["task_usage_start_time" , "task_usage_end_time" , "task_usage_job_id" , "task_usage_tanks_index" , "task_usage_machine_id" , "task_usage_CPU_rate" , "task_usage_canonical_usage_memory" , "task_usage_assigned_usage_memory" , "task_usage_unmapped_page_cache" , "task_usage_total_page_cache" , "task_usage_maximum_usage_memory" , "task_usage_disk_time" , "task_usage_local_disk_space" , "task_usage_max_CPU_rate" , "task_usage_max_disk_time" , "task_usage_cicles_x_instuction" , "task_usage_memory_accesses_x_instruction" , "task_usage_simple_partition" , "task_usage_agregation_type" , "task_usage_sampled_CPU_usage" , "task_usage_clasificacio_CPU_uso" , "task_usage_vivo_muerto" , "gt_30_days","gt_30_days","gt_180_days","dias_de_uso"]
    
#     class Meta:
#         model = task_usage

# admin.site.register(task_event, task_events_Admin)
# admin.site.register(task_usage, task_usage_Admin)
admin.site.register(Previo)
admin.site.register(CSV)