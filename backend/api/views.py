from rest_framework.viewsets import ModelViewSet


class MultiSerializerModelViewSet(ModelViewSet):
    serializer_dict = {}

    def get_serializer_class(self):
        return self.serializer_dict.get(self.action, self.serializer_class)
