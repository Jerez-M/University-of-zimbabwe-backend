# from celery import shared_task
# from django.core.mail import send_mail
# from django.conf import settings

# @shared_task
# def send_registration_email(full_name, username, password, altEmail):
#     email_subject = "Welcome to the UZ Recruitment Portal, Your Account has been Created Successifully"
#     email_to = altEmail
#     email_from = settings.EMAIL_HOST_USER
#     email_body = f"Dear {full_name},\n\nWe are delighted to inform you that your account has been successfully created for the UZ Recruitment Portal. " \
#                  f"You can now access your account using the following details:\n\n" \
#                  f"Username: {username}\n" \
#                  f"Password: {password}\n" \
#                  f"Email: {altEmail}\n" \
#                  f"Role: APPLICANT\n\n" \
#                  f"Kindly use the Username and password above to Sign in to your account. \n \n" \
#                  f"Please keep this information secure and do not share it with anyone. If you have any questions or need assistance, " \
#                  f"feel free to reach out to our support team at uzrecruitment@uz.ac.zw.\n\n" \
#                  f"Thank you for joining UZ Recruitment Portal. We look forward to providing you with a great experience!\n\n" \
#                  f"Best regards,\n" \
#                  f"University Of Zimbabwe\n"

#     send_mail(email_subject, email_body, email_from, [email_to], fail_silently=True)