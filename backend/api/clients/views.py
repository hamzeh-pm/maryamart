from accounts.models import Account
from accounts.serializers import ClientSerializer, ClientUpdateSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..views import MultiSerializerModelViewSet


class ClientViewSet(MultiSerializerModelViewSet):
    queryset = Account.objects.all()
    serializer_class = ClientSerializer
    serializer_dict = {"update": ClientUpdateSerializer}

    def list(self, request, *args, **kwargs):
        """
        See the list of clients - disabled in this path
        """
        resp = {"message": "list view is not provided in this path"}
        return Response(resp, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [
                AllowAny
            ]  # TODO change it so only the client owner can use it
        return [permission() for permission in permission_classes]
