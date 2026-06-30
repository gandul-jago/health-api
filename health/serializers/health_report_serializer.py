from rest_framework import serializers
from health.models import HealthReport


class HealthReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthReport
        fields = "__all__"

class HealthReportDetailSerializer(serializers.ModelSerializer):

    patient = serializers.StringRelatedField()
    disease = serializers.StringRelatedField()
    symptoms = serializers.StringRelatedField(many=True)

    class Meta:
        model = HealthReport
        fields = "__all__"