from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from shop.models import Factory, Retail, Entrepreneur
from shop.serializers import FactorySerializers, FactorySerializersList, RetailSerializers, RetailSerializersList, \
    EntrepreneurSerializers, EntrepreneurSerializersList
from django_filters.rest_framework import DjangoFilterBackend


class FactoryCreateApiView(generics.CreateAPIView):
    serializer_class = FactorySerializers
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_factory = serializer.save(user=self.request.user)


class FactoryListApiView(generics.ListAPIView):
    serializer_class = FactorySerializersList
    queryset = Factory.objects.all()


class RetailCreateApiView(generics.CreateAPIView):
    serializer_class = RetailSerializers
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_factory = serializer.save(user=self.request.user)


class RetailListApiView(generics.ListAPIView):
    serializer_class = RetailSerializersList
    queryset = Retail.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('user__city',)


class EntrepreneurCreateApiView(generics.CreateAPIView):
    serializer_class = EntrepreneurSerializers
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_factory = serializer.save(user=self.request.user)


class EntrepreneurListApiView(generics.ListAPIView):
    serializer_class = EntrepreneurSerializersList
    queryset = Entrepreneur.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('user__city',)


class EntrepreneurDestroyApiView(generics.DestroyAPIView):
    serializer_class = EntrepreneurSerializersList
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsAuthenticated]


class EntrepreneurUpdateApiView(generics.UpdateAPIView):
    serializer_class = EntrepreneurSerializers
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsAuthenticated]


class RetailDestroyApiView(generics.DestroyAPIView):
    serializer_class = RetailSerializers
    queryset = Retail.objects.all()
    permission_classes = [IsAuthenticated]


class RetailUpdateApiView(generics.UpdateAPIView):
    serializer_class = RetailSerializers
    queryset = Retail.objects.all()
    permission_classes = [IsAuthenticated]