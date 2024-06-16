from django.contrib import admin

# Register your models here.

from .models import Patient,PatientUpdate,TreatmentPlan, Doctor, Appointment, Invoice, Report

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Invoice)
admin.site.register(Report)
admin.site.register(PatientUpdate)
admin.site.register(TreatmentPlan)
