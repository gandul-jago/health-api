from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from health.models import HealthReport
from health.serializers import (
    HealthReportSerializer,
    HealthReportDetailSerializer,
)
from health.models import HealthReport, Status


class HealthReportList(APIView):

    def get(self, request):
        report = HealthReport.objects.filter(status__name="Aktif")
        serializer = HealthReportDetailSerializer(report, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HealthReportSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HealthReportDetail(APIView):

    def get_object(self, pk):
        return HealthReport.objects.get(
            pk=pk,
            status__name="Aktif"
        )

    def get(self, request, pk):
        report = self.get_object(pk)
        serializer = HealthReportDetailSerializer(report)
        return Response(serializer.data)

    def put(self, request, pk):
        report = self.get_object(pk)
        serializer = HealthReportSerializer(report, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        report = self.get_object(pk)
        serializer = HealthReportSerializer(report, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        report = self.get_object(pk)
        deleted_status = Status.objects.get(name="DIHAPUS")
        report.status = deleted_status
        report.save()
        return Response(
            {"message": "Data berhasil dihapus"},
            status=status.HTTP_200_OK
        )