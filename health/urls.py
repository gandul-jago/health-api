from django.urls import path

from .views import (
    PatientList,
    PatientDetail,
    DiseaseList,
    DiseaseDetail,
    SymptomList,
    SymptomDetail,
    HealthReportList,
    HealthReportDetail,
)

urlpatterns = [

    # Patient
    path('patients/', PatientList.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetail.as_view(), name='patient-detail'),

    # Disease
    path('diseases/', DiseaseList.as_view(), name='disease-list'),
    path('diseases/<int:pk>/', DiseaseDetail.as_view(), name='disease-detail'),

    # Symptom
    path('symptoms/', SymptomList.as_view(), name='symptom-list'),
    path('symptoms/<int:pk>/', SymptomDetail.as_view(), name='symptom-detail'),

    # Health Report
    path('health-reports/', HealthReportList.as_view(), name='health-report-list'),
    path('health-reports/<int:pk>/', HealthReportDetail.as_view(), name='health-report-detail'),

]