from audit_trail_engine.helpers import audit_trail
from .serializers import ApplicantWorkExperienceSerializer
from ..models import Applicant, ApplicantWorkExperience
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status

# Create your views here.

class ApplicantWorkExperienceCreate(GenericAPIView):
    permission_classes = []
    serializer_class = ApplicantWorkExperienceSerializer
    queryset = ApplicantWorkExperience.objects.all()

    def post(self, request):
        data = {
            'applicant': request.data['applicant'],
            'employer': request.data['employer'],
            'job_title': request.data['job_title'],
            'job_description': request.data['job_description'],
            'start_date': request.data['start_date'],
            'end_date': request.data['end_date'],
            'reference_contacts_1': request.data['reference_contacts_1'],
            'reference_contacts_2': request.data['reference_contacts_2']
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            saved = serializer.save()
            # audit_trail(
            #     request.user.id,
            #     f'Create Applicant work experience {saved.Applicant.user.firstName} '
            #     f'{saved.Applicant.user.lastName}',
            #     'ApplicantWorkExperience',
            #     saved.id,
            #     'Create'
            # )
            data = {
                "data": serializer.data,
                "message": "Applicant work experiance created successifully"
            }
            return Response(data, status=status.HTTP_201_CREATED)


class ApplicantWorkExperienceGetAll(GenericAPIView):
    permission_classes = []
    serializer_class = ApplicantWorkExperienceSerializer
    queryset = ApplicantWorkExperience.objects.all()

    def get(self, request):
        experience = self.queryset.all()
        serializer = self.serializer_class(experience, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ApplicantWorkExperienceGetUpdateDeleteByID(GenericAPIView):
    permission_classes = []
    serializer_class = ApplicantWorkExperienceSerializer
    queryset = ApplicantWorkExperience.objects.all()

    def get(self, request, pk):
        try:
            experience = self.queryset.get(pk=pk)
        except ApplicantWorkExperience.DoesNotExist:
            return Response(data={'error': 'Applicant Staff Work Experience not Found.'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = self.serializer_class(experience)
            return Response(data=serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        try:
            experience = self.queryset.get(pk=pk)
        except ApplicantWorkExperience.DoesNotExist:
            return Response(data={'error': 'Applicant Staff Work Experience not Found.'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = self.serializer_class(experience, data=request.data, partial=True)
            if serializer.is_valid():
                saved = serializer.save()
                # audit_trail(
                #     request.user.id,
                #     f'Update Applicant work experience {saved.Applicant.user.firstName} '
                #     f'{saved.Applicant.user.lastName}',
                #     'ApplicantWorkExperience',
                #     saved.id,
                #     'Update'
                # )
                data = {
                    "data": serializer.data,
                    "message": "Applicant work experiance created successifully"
                }
                return Response(data, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            experience = self.queryset.get(pk=pk)
        except ApplicantWorkExperience.DoesNotExist:
            return Response(data={'error': 'Applicant Staff Work Experience not Found.'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            # audit_trail(
            #     request.user.id,
            #     f'Delete Applicant work experience {experience.Applicant.user.firstName} '
            #     f'{experience.Applicant.user.lastName}',
            #     'ApplicantWorkExperience',
            #     experience.id,
            #     'Delete'
            # )
            experience.delete()
            return Response(data={'message': 'Applicant Staff Work Experience deleted successfully.'},
                            status=status.HTTP_204_NO_CONTENT)
