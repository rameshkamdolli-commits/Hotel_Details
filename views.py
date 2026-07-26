from rest_framework import viewsets
from.models import HotelDetails
from.serializers import HotelDetailsSerializer

class HotelDetailsViewSet (viewsets.ModelViewSet):
    queryset = HotelDetails.objects.all().order_by('-created_at')
    serializer_class = HotelDetailsSerializer