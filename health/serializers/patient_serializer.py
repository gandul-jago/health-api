from rest_framework import serializers
from health.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Patient
        fields = "__all__"