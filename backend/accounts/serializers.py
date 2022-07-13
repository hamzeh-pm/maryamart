from rest_framework import serializers

from .models import Account


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["email", "mobile", "name", "role", "password"]
        extra_kwargs = {"password": {"write_only": True}, "role": {"read_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        client = Account(is_active=False, **validated_data)
        client.set_password(password)
        client.save()
        return client
