from rest_framework import serializers
from .models import Applicant
from accounts.models import User
from django.contrib.auth.models import Group, Permission


class ApplicantUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["role", "is_superuser", "is_staff", "is_active", "institution_email"]

        extra_kwargs = {'password': {'write_only': True, 'required': True},
                        "institution": {"required": True},
                        "username": {"required": True},
                        "first_name": {"required": True},
                        "last_name": {"required": True},
                        "gender": {"required": True},
                        "phone_number_1": {"required": True},
                        "national_id": {"required": True},
                        "nationality": {"required": True},
                        "home_address": {"required": True},
                        "altEmail": {"required": True},
                        }


class RetrieveApplicantUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["institution_email"]

        extra_kwargs = {
            "password": {"write_only": True}
        }


class ApplicantSerializer(serializers.ModelSerializer):
    user = ApplicantUserSerializer()

    class Meta:
        model = Applicant
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        groups_data = user_data.pop('groups', [])
        permissions_data = user_data.pop('user_permissions', [])

        user = User.objects.create(**user_data)
        
        user.role = 'APPLICANT'
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.set_password(password)

        try:
            applicant = Applicant.objects.create(user=user, **validated_data)
            user.save()

            groups = Group.objects.filter(id__in=[group_data['id'] for group_data in groups_data])
            applicant.user.groups.set(groups)

            permissions = Permission.objects.filter(id__in=[perm_data['id'] for perm_data in permissions_data])
            applicant.user.user_permissions.set(permissions)

            applicant.save()
            return applicant

        except Exception as e:
            user.delete()  # Delete the user if applicant creation fails
            raise e  # Re-raise the exception

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        groups_data = user_data.pop('groups', [])
        permissions_data = user_data.pop('user_permissions', [])

        if user_data:
            user = instance.user
            for key, value in user_data.items():
                setattr(user, key, value)
            user.save()

        if groups_data:
            groups = Group.objects.filter(id__in=[group_data['id'] for group_data in groups_data])
            instance.user.groups.set(groups)

        if permissions_data:
            permissions = Permission.objects.filter(id__in=[perm_data['id'] for perm_data in permissions_data])
            instance.user.user_permissions.set(permissions)

        return super().update(instance, validated_data)
    

class ApplicantRetrieveSerializer(serializers.ModelSerializer):
    user = RetrieveApplicantUserSerializer()

    class Meta:
        model = Applicant
        fields = "__all__"


    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        groups_data = user_data.pop('groups', [])
        permissions_data = user_data.pop('user_permissions', [])

        if user_data:
            user = instance.user
            for key, value in user_data.items():
                setattr(user, key, value)
            user.save()

        if groups_data:
            groups = Group.objects.filter(id__in=[group_data['id'] for group_data in groups_data])
            instance.user.groups.set(groups)

        if permissions_data:
            permissions = Permission.objects.filter(id__in=[perm_data['id'] for perm_data in permissions_data])
            instance.user.user_permissions.set(permissions)

        return super().update(instance, validated_data)
    
class ApplicantUploadProfPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['applicant', 'file']