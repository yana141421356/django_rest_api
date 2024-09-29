from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status   # 追加
from .models import Item, Address
from .serializers import ItemSerializer, ItemDescriptionSerializer, AddressSerializer
from django.shortcuts import get_object_or_404

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

@api_view(['GET'])
def item_description_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    serializer = ItemDescriptionSerializer(item)
    return Response(serializer.data, status=status.HTTP_200_OK)

    
    
