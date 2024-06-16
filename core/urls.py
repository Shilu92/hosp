
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path('patients/new/', views.patient_create, name='patient_create'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patient-updates/new/', views.patientupdate_create, name='patientupdate_create'),
    path('treatment-plans/new/', views.treatmentplan_create, name='treatmentplan_create'),
    path('doctors/new/', views.doctor_create, name='doctor_create'),
    path('appointments/new/', views.appointment_create, name='appointment_create'),
    path('invoices/new/', views.invoice_create, name='invoice_create'),
    path('reports/new/', views.report_create, name='report_create'),
   
]