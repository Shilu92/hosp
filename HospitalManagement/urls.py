"""
URL configuration for HospitalManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from core.views import PatientViewSet,PatientUpdateViewSet, DoctorViewSet, AppointmentViewSet, InvoiceViewSet, ReportViewSet,TreatmentPlanViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'patientupdate', PatientUpdateViewSet)
router.register(r'treatment-plans', TreatmentPlanViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('dashboard/', include(('django_plotly_dash.urls', 'the_django_plotly_dash'))),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)