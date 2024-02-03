from .serializers import SuperuserSerializer, SuperuserRetrieveSerializer
from .models import Superuser
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import status
from django.conf import settings
from accounts.models import User
from django.core.mail import send_mail

# Create your views here.


class CreateSuperuserView(CreateAPIView):
    permission_classes = []
    serializer_class = SuperuserSerializer
    queryset = Superuser.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:

            if serializer.is_valid():
                self.perform_create(serializer)
                data = {
                    "message": "Superuser created successifully",
                    "data": serializer.data
                }
                
                first_name = serializer.validated_data['user']['first_name'].upper()
                last_name = serializer.validated_data['user']['last_name'].upper()
                # username = serializer.validated_data['user']['username']
                altEmail = serializer.validated_data['user']['altEmail']
                institution_email = serializer.validated_data['user']['institution_email']
                full_name = f'{first_name } { last_name}'
                password = 'password'

                this_instance = User.objects.get(pk=serializer.data['user']['id'])
                username = this_instance.username
                role = this_instance.role


                email_subject = f"Welcome to the UZ Recruitment Portal, Your Account has been Created Successifully"
                email_to = institution_email
                email_to_2 = altEmail
                email_from = settings.EMAIL_HOST_USER
                email_body = f"Dear {full_name},\n\nWe are delighted to inform you that your account has been successfully created for the UZ Recruitment Portal. " \
                            f"You can now access your account using the following details:\n\n" \
                            f"Username: {username}\n" \
                            f"Password: {password}\n"\
                            f"Institution Email: {institution_email}\n" \
                            f"Personal Email: {altEmail}\n" \
                            f"Role: {role}\n\n" \
                            f"Kindly use the Username and password above to Sign in to your account. \n \n" \
                            f"Please keep this information secure and do not share it with anyone. If you have any questions or need assistance, " \
                            f"feel free to reach out to our support team at uzrecruitment@uz.ac.zw.\n\n" \
                            f"Thank you for joining UZ Recruitment Portal. We look forward to providing you with a great experience!\n\n" \
                            f"Best regards,\n" \
                            f"University Of Zimbabwe\n"  
                                                          
                send_mail(email_subject, email_body, email_from, [email_to, email_to_2], fail_silently=True)
                return Response(data, status=status.HTTP_201_CREATED)

            return Response({"message": "Failed to create superuser, Validation error occured.", "error": serializer.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message": "Failed to create superuser. Exception error occured", "error": str(e)}, 
                            status=status.HTTP_400_BAD_REQUEST)
        

class GetAllSuperusers(ListAPIView):
    permission_classes = []
    serializer_class = SuperuserRetrieveSerializer
    queryset = Superuser.objects.all()


class SuperuserReadUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = SuperuserRetrieveSerializer
    queryset = Superuser.objects.all()

