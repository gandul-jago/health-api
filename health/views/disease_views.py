from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from health.models import Disease
from health.serializers import DiseaseSerializer
from health.models import Disease, Status


class DiseaseList(APIView):

    def get(self, request):
        disease = Disease.objects.filter(status__name="Aktif")
        serializer = DiseaseSerializer(disease, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiseaseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiseaseDetail(APIView):

    def get_object(self, pk):
        return Disease.objects.get(
            pk=pk,
            status__name="Aktif"
        )

    def get(self, request, pk):
        disease = self.get_object(pk)
        serializer = DiseaseSerializer(disease)
        return Response(serializer.data)

    def put(self, request, pk):
        disease = self.get_object(pk)
        serializer = DiseaseSerializer(disease, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        disease = self.get_object(pk)
        serializer = DiseaseSerializer(disease, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        disease = self.get_object(pk)
        deleted_status = Status.objects.get(name="Dihapus")
        disease.status = deleted_status
        disease.save()
    
        return Response(
            {"message": "Data berhasil Dihapus"},
            status=status.HTTP_200_OK
        )