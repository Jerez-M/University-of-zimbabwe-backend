from audit_trail_engine.helpers import audit_trail
from .serializers import ApplicantPersonalDocumentSerializer
from ..models import ApplicantPersonalDocument
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

# Create your views here.



class ApplicantPersonalDocumentCreate(GenericAPIView):
    permission_classes = []
    serializer_class = ApplicantPersonalDocumentSerializer
    queryset = ApplicantPersonalDocument.objects.all()

    def post(self, request):
        data = {
            'applicant': request.data['applicant'],
            'doc_type': request.data['doc_type']
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            saved = serializer.save()
            # audit_trail(
            #     request.user.id,
            #     f'Create applicant personal document record {saved.Applicant.user.firstName} '
            #     f'{saved.Applicant.user.lastName}',
            #     'ApplicantPersonalDocument',
            #     saved.id,
            #     'Create'
            # )
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ApplicantPersonalDocumentGetAll(GenericAPIView):
    permission_classes = []
    serializer_class = ApplicantPersonalDocumentSerializer
    queryset = ApplicantPersonalDocument.objects.all()

    def get(self, request):
        experience = self.queryset.all()
        serializer = self.serializer_class(experience, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([])
def update_staff_personal_document(request, Id):
    if request.method == 'POST':
        try:
            personal_doc = ApplicantPersonalDocument.objects.get(applicant_id=Id)
        except ApplicantPersonalDocument.DoesNotExist:
            return Response(data={'error': 'Applicant personal document record not Found.'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                dp = request.FILES['file']
            except KeyError:
                return Response(data={'error': 'Applicant Document missing.'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                dp.name = f'{personal_doc.applicant.user.username}.{dp.name.split(".")[1]}'
                personal_doc.file = dp
                personal_doc.save()
                # audit_trail(
                #     request.user.id,
                #     f'Upload Applicant personal document {personal_doc.applicant.user.first_name} '
                #     f'{personal_doc.applicant.user.last_name}',
                #     'ApplicantPersonalDocument',
                #     personal_doc.id,
                #     'Update'
                # )
                return Response(data={'message': 'Applicant member personal document updated successfully.'},
                                status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ApplicantPersonalDocumentUpdateGetDeleteByID(GenericAPIView):
    permission_classes = []
    serializer_class = ApplicantPersonalDocumentSerializer
    queryset = ApplicantPersonalDocument.objects.all()

    def get(self, request, pk):
        try:
            personal_doc = self.queryset.get(pk=pk)
        except ApplicantPersonalDocument.DoesNotExist:
            return Response(data={'error': 'Applicant Work Experience not Found.'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = self.serializer_class(personal_doc)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            personal_doc = self.queryset.get(pk=pk)
        except ApplicantPersonalDocument.DoesNotExist:
            return Response(data={'error': 'Applicant Work Experience not Found.'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = self.serializer_class(personal_doc, data=request.data, partial=True)
            if serializer.is_valid():
                saved = serializer.save()
                # audit_trail(
                #     request.user.id,
                #     f'Update Applicant personal document record {saved.applicant.user.first_name} '
                #     f'{saved.applicant.user.last_name}',
                #     'ApplicantPersonalDocument',
                #     saved.id,
                #     'Update'
                # )
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            personal_doc = self.queryset.get(pk=pk)
        except ApplicantPersonalDocument.DoesNotExist:
            return Response(data={'error': 'Applicant Work Experience not Found.'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            # audit_trail(
            #     request.user.id,
            #     f'Delete Applicant personal document record {personal_doc.applicant.user.first_name} '
            #     f'{personal_doc.applicant.user.last_name}',
            #     'ApplicantPersonalDocument',
            #     personal_doc.id,
            #     'Delete'
            # )
            personal_doc.delete()
            return Response(data={'message': 'Applicant Work Experience deleted successfully.'},
                            status=status.HTTP_204_NO_CONTENT)
