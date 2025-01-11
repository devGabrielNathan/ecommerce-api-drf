from rest_framework import generics

from ecommerce.users.models.supplier import Supplier
from ecommerce.users.serializers.supplier import SupplierSerializer


# Create your views here.
class SupplierGenericListCreate(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierGenericRetrieveUpdateDestroy(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
