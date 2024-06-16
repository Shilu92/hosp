from django_plotly_dash.views import DjangoDash
from dash import dcc, html
from core.models import Patient, TreatmentPlan
from datetime import datetime, timedelta

# Create a new DjangoDash instance
app_name = 'new_dashboard'
app = DjangoDash(name=app_name)

# Define layout
app.layout = html.Div([
    html.H1('Hospital Management System Dashboard'),
    html.Div([
        dcc.Graph(
            id='patient-growth-chart',
            figure={
                'data': [
                    {'x': [patient.user.get_full_name() for patient in Patient.objects.all()], 
                     'y': [patient.age for patient in Patient.objects.all()], 
                     'type': 'bar', 'name': 'Age'},
                ],
                'layout': {
                    'title': 'Patients Age Distribution'
                }
            }
        ),
        dcc.Graph(
            id='treatment-plan-status',
            figure={
                'data': [
                    {'x': [plan.start_date for plan in TreatmentPlan.objects.all()], 
                     'y': [plan.progress for plan in TreatmentPlan.objects.all()], 
                     'type': 'scatter', 'mode': 'lines+markers', 'name': 'Progress'},
                ],
                'layout': {
                    'title': 'Treatment Plan Progress'
                }
            }
        ),
    ]),
])