from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from InfoPage.models import InfoUnit
from api.serializers import InfoUnitSerializer


@api_view(['GET'])
def infounit_list(request):
    
    if request.method == 'GET':
        InfoUnits = InfoUnit.objects.all()
        serializer = InfoUnitSerializer(InfoUnits, many=True)
        return Response(serializer.data)

    """

    POST request here: 

    elif request.method == 'POST':
        serializer = InfoUnitSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """

@api_view(['GET'])
def infounit_detail(request, pk):
    global InfoUnit
    try:
        InfoUnit = InfoUnit.objects.get(pk=pk)
    except InfoUnit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InfoUnitSerializer(InfoUnit)
        return Response(serializer.data)
    
    """
    
    POST and DELETE requests here:

    elif request.method == 'PUT':
        serializer = InfoUnitSerializer(InfoUnit, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        InfoUnit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    """
