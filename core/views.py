
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Patient,TreatmentPlan, Doctor, Appointment, Invoice, Report,PatientUpdate
from .serializers import PatientSerializer,TreatmentPlanSerializer, DoctorSerializer, AppointmentSerializer, InvoiceSerializer, ReportSerializer,PatientUpdateSerializer
from .forms import PatientForm, PatientUpdateForm, TreatmentPlanForm, DoctorForm, AppointmentForm, InvoiceForm, ReportForm

def home(request):
    return render(request, 'index.html')


def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patient_form.html', {'form': form})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient_detail.html', {'patient': patient})

def patientupdate_create(request):
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patientupdate_list')
    else:
        form = PatientUpdateForm()
    return render(request, 'patient_updateform.html', {'form': form})

def patientupdate_list(request):
    patientupdates = PatientUpdate.objects.all()
    return render(request, 'patientupdate_list.html', {'patientupdates': patientupdates})

def patientupdate_detail(request, pk):
    patientupdate = get_object_or_404(PatientUpdate, pk=pk)
    return render(request, 'patientupdate_detail.html', {'patientupdate': patientupdate})

# Add similar views for TreatmentPlan, Doctor, Appointment, Invoice, and Report

def treatmentplan_create(request):
    if request.method == 'POST':
        form = TreatmentPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('treatmentplan_list')
    else:
        form = TreatmentPlanForm()
    return render(request, 'treatmentplan_form.html', {'form': form})

def treatmentplan_list(request):
    treatmentplans = TreatmentPlan.objects.all()
    return render(request, 'treatmentplan_list.html', {'treatmentplans': treatmentplans})

def treatmentplan_detail(request, pk):
    treatmentplan = get_object_or_404(TreatmentPlan, pk=pk)
    return render(request, 'treatmentplan_detail.html', {'treatmentplan': treatmentplan})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctor_form.html', {'form': form})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctor_detail.html', {'doctor': doctor})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointment_detail.html', {'appointment': appointment})

def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'invoice_form.html', {'form': form})

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoice_list.html', {'invoices': invoices})

def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'invoice_detail.html', {'invoice': invoice})

def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm()
    return render(request, 'report_form.html', {'form': form})

def report_list(request):
    reports = Report.objects.all()
    return render(request, 'report_list.html', {'reports': reports})

def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'report_detail.html', {'report': report})


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientUpdateViewSet(viewsets.ModelViewSet):
    queryset = PatientUpdate.objects.all()
    serializer_class = PatientUpdateSerializer

class TreatmentPlanViewSet(viewsets.ModelViewSet):
    queryset = TreatmentPlan.objects.all()
    serializer_class = TreatmentPlanSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer



def dashboard_view(request):
    return render(request, 'dashboard/dashboard2.html')