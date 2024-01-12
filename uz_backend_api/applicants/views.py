from .serializers import ApplicantSerializer, ApplicantRetrieveSerializer
from .models import Applicant
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from accounts.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

class CreateApplicantView(CreateAPIView):
    permission_classes = []
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        try:
            if serializer.is_valid():

                self.perform_create(serializer)
                data = {
                    "message": "Applicant created successifully",
                    "data": serializer.data
                }

                return Response(data, status=status.HTTP_201_CREATED)

            return Response({"message": "Failed to create applicant, Validation error occured.", "error": serializer.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message": "Failed to create applicant. Exception error occured", "error": str(e)}, 
                            status=status.HTTP_400_BAD_REQUEST)
        

class GetAllApplicants(ListAPIView):
    permission_classes = []
    serializer_class = ApplicantRetrieveSerializer
    queryset = Applicant.objects.all()


class ApplicantReadUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = ApplicantRetrieveSerializer
    queryset = Applicant.objects.all()

