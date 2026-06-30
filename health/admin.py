from django.contrib import admin
from .models import Patient, Disease, Symptom, HealthReport, Status

#endpoin pasien
admin.site.register(Patient)
#endpoint penyakit
admin.site.register(Disease)
#endpoint gejala
admin.site.register(Symptom)
#endpioint laporan kesehatan
admin.site.register(HealthReport)
#endpoint status
admin.site.register(Status) 