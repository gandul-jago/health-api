from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from health.models import Patient
from health.serializers import PatientSerializer
from health.models import Patient, Status


class PatientList(APIView):

    def get(self, request):
        patient = Patient.objects.filter(status__name="Aktif")
        serializer = PatientSerializer(patient, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDetail(APIView):

    def get_object(self, pk):
        return Patient.objects.get(
            pk=pk,
            status__name="Aktif"
        )

    def get(self, request, pk):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        patient = self.get_object(pk)

        deleted_status = Status.objects.get(name="Dihapus")
        patient.status = deleted_status
        patient.save()

        return Response(
            {"message": "Data berhasil Dihapus"},
            status=status.HTTP_200_OK
        )