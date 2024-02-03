from audit_trail_engine.helpers import audit_trail
from .serializers import ApplicantEducationalQualificationSerializer
from ..models import EducationalQualification
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# Create your views here.


class EducationalQualificationCreate(GenericAPIView):
    permission_classes = []
    serializer_class = ApplicantEducationalQualificationSerializer
    queryset = EducationalQualification.objects.all()

    def post(self, request):
        data = {
            'applicant': request.data['applicant'],
            'institution_attended': request.data['institution_attended'],
            'level': request.data['level'],
            'qualification': request.data['qualification'],
            'description': request.data['description'],
            'start_date': request.data['start_date'],
            'end_date': request.data['end_date']
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            saved = serializer.save()
            # audit_trail(
            #     request.user.id,
            #     f'Create Applicant Educational {saved.Applicant.user.firstName} {saved.Applicant.user.lastName}',
            #     'Educational',
            #     saved.id,
            #     'Create'
            # )
            data = {
                "message": "Qualification added successifully",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)


class ApplicantEducationalQualificationGetAll(GenericAPIView):
    permission_classes = []
    serializer_class = ApplicantEducationalQualificationSerializer
    queryset = EducationalQualification.objects.all()

    def get(self, request):
        education = self.queryset.all()
        serializer = self.serializer_class(education, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([])
def update_applicant_educational_documents(request, Id):
    if request.method == 'POST':
        try:
            qualification = EducationalQualification.objects.get(applicant_id=Id)
        except EducationalQualification.DoesNotExist:
            return Response(data={'error': 'Applicant educational qualification not Found.'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                dp = request.FILES['file']
            except KeyError:
                return Response(data={'error': 'Applicant Document missing.'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                dp.name = f'{qualification.applicant.user.username}.{dp.name.split(".")[1]}'
                qualification.file = dp

                qualification.save()
                # audit_trail(
                #     request.user.id,
                #     f'Upload Applicant educational documents {qualification.applicant.user.first_name} for level '
                #     f'{qualification.applicant.user.last_name}',
                #     'Educational',
                #     qualification.id,
                #     'Create'
                # )
                return Response(data={'message': 'Applicant member educational qualification updated successfully.'},
                                status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class EducationalQualificationUpdateDelete(GenericAPIView):
    permission_classes = []
    serializer_class = ApplicantEducationalQualificationSerializer
    queryset = EducationalQualification.objects.all()

    def put(self, request, pk):
        try:
            qualification = self.queryset.get(pk=pk)
        except EducationalQualification.DoesNotExist:
            return Response(data={'error': 'Applicant educational qualification not Found.'},
                            status=status.HTTP_404_NOT_FOUND)
        else:

            serializer = self.serializer_class(qualification, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                # audit_trail(
                #     request.user.id,
                #     f'Update Applicant educational {qualification.applicant.user.first_name} '
                #     f'{qualification.applicant.user.last_name}',
                #     'Educational',
                #     qualification.id,
                #     'Create'
                # )
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
            qualification = self.queryset.get(pk=pk)
        except EducationalQualification.DoesNotExist:
            return Response(data={'error': 'Applicant educational qualification not Found.'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = self.serializer_class(qualification)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            qualification = self.queryset.get(pk=pk)
        except EducationalQualification.DoesNotExist:
            return Response(data={'error': 'Applicant educational qualification not Found.'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            # audit_trail(
            #     request.user.id,
            #     f'Delete Applicant educational {qualification.Applicant.user.firstName} '
            #     f'{qualification.Applicant.user.lastName}',
            #     'Educational',
            #     qualification.id,
            #     'Delete'
            # )
            qualification.delete()
            return Response(data={'message': 'Applicant educational qualification deleted successfully.'},
                            status=status.HTTP_204_NO_CONTENT)

