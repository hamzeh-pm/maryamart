from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Account


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["email", "mobile", "name", "role", "password"]
        extra_kwargs = {"password": {"write_only": True}, "role": {"read_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        client = Account(**validated_data)
        client.set_password(password)
        client.save()

        # Create client group and set permission
        client_group, created = Group.objects.get_or_create(name="client")
        client.groups.add(client_group)

        # Default permission have to add to this group here

        return client
