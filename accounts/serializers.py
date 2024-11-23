# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserAttribute
from .services.recommendation import UserRecommendationService
from django.contrib.auth.models import User, Group

from .models import UserAttribute,UserGroup


class UserRegistrationSerializer(serializers.ModelSerializer):
    attributes = serializers.ListField(
        child=serializers.CharField(max_length=100),
        write_only=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'attributes']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        attributes = validated_data.pop('attributes', [])
        print("Attributes from request:", attributes)


        # Create user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'], 
            password=validated_data['password']
        )

        # Create user attributes
        user_attributes = UserAttribute.objects.create(
            user=user,
            attributes=attributes
        )

        # Assign groups or handle no group scenario
        self.assign_groups(user_attributes, attributes)

        return user

    def assign_groups(self, user_attributes, attributes):
        
        # Fetch all groups
        groups = UserGroup.objects.all()
        print("skander")
        for group in groups:
          for member in group.members.all():
            if set(attributes) & set(member.attributes):
                group.members.add(user_attributes)
                return  # User added to an existing group

        # If no match found, create a new group
        new_group = UserGroup.objects.create()
        new_group.members.add(user_attributes)
class GroupSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()

    class Meta:
        model = UserGroup
        fields = ['id', 'created_at', 'members']

    def get_members(self, group):
        members = group.members.all()
        return [
            {
                "user": member.user.id,
                "attributes": member.attributes,
            }
            for member in members
        ]
