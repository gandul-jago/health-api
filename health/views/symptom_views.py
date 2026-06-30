from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from health.models import Symptom
from health.serializers import SymptomSerializer
from health.models import Symptom, Status


class SymptomList(APIView):

    def get(self, request):
        symptom = Symptom.objects.filter(status__name="Aktif")
        serializer = SymptomSerializer(symptom, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SymptomSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SymptomDetail(APIView):

    def get_object(self, pk):
        return Symptom.objects.get(
            pk=pk,
            status__name="Aktif"
        )

    def get(self, request, pk):
        symptom = self.get_object(pk)
        serializer = SymptomSerializer(symptom)
        return Response(serializer.data)

    def put(self, request, pk):
        symptom = self.get_object(pk)
        serializer = SymptomSerializer(symptom, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        symptom = self.get_object(pk)
        serializer = SymptomSerializer(symptom, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        symptom = self.get_object(pk)
        deleted_status = Status.objects.get(name="Dihapus")
        symptom.status = deleted_status
        symptom.save()
        return Response(
            {"message": "Data berhasil Dihapus"},
            status=status.HTTP_200_OK
        )