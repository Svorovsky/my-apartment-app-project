from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from InfoPage.models import InfoUnit
from api.serializers import InfoUnitSerializer

from Delivery.models import DeliveryService
from api.serializers import DeliveryServiceSerializer

from News.models import NewsItem
from api.serializers import NewsItemSerializer

from Services.models import Service
from api.serializers import ServiceSerializer

from GuestPass.models import Guest, GuestPass
from api.serializers import GuestSerializer, GuestPassSerializer

from MyBills.models import Bill, PersonalBill
from api.serializers import PersonalBillSerializer

from UserProfile.models import Person
from api.serializers import PersonSerializer

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


#InfoUnit api functions here:

@api_view(['GET'])
def infounit_list(request):
    global InfoUnit
    """
    List all infounits.
    """
    if request.method == 'GET':
        infounits = InfoUnit.objects.all()
        serializer = InfoUnitSerializer(infounits, many=True)
        return Response(serializer.data)

    """

    POST request: 

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
    """
    Get a specific infounit.
    """
    try:
        infounit = InfoUnit.objects.get(pk=pk)
    except InfoUnit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InfoUnitSerializer(infounit)
        return Response(serializer.data)
    
    """
    
    PUT and DELETE requests:

    elif request.method == 'PUT':
        serializer = InfoUnitSerializer(infounit, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        infounit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    """

#DeliveryService api functions here:

@api_view(['GET'])
def deliveryservice_list(request):
    global DeliveryService
    """
    List all deliveryservices.
    """
    if request.method == 'GET':
        deliveryservices = DeliveryService.objects.all()
        serializer = DeliveryServiceSerializer(deliveryservices, many=True)
        return Response(serializer.data)

    """

    POST request:
   
    elif request.method == 'POST':
        serializer = DeliveryServiceSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """

@api_view(['GET'])
def deliveryservice_detail(request, pk):
    global DeliveryService
    """
    Get a specific deliveryservice.
    """
    try:
        deliveryservice = DeliveryService.objects.get(pk=pk)
    except DeliveryService.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeliveryServiceSerializer(deliveryservice)
        return Response(serializer.data)

    """

    PUT and DELETE requests:

    elif request.method == 'PUT':
        serializer = DeliveryServiceSerializer(deliveryservice, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        deliveryservice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    """

#NewsItem api functions here:

@api_view(['GET'])
def newsitem_list(request):
    global NewsItem
    """
    List all newsitems.
    """
    if request.method == 'GET':
        newsitems = NewsItem.objects.all()
        serializer = NewsItemSerializer(newsitems, many=True)
        return Response(serializer.data)

    """

    POST request: 

    elif request.method == 'POST':
        serializer = NewsItemSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """

@api_view(['GET'])
def newsitem_detail(request, pk):
    global NewsItem
    """
    Get a specific newsitem.
    """
    try:
        newsitem = NewsItem.objects.get(pk=pk)
    except NewsItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NewsItemSerializer(newsitem)
        return Response(serializer.data)

    """
    
    PUT and DELETE requests:

    elif request.method == 'PUT':
        serializer = NewsItemSerializer(newsitem, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        newsitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    """

#Service api functions here:

@api_view(['GET'])
def service_list(request):
    global Service
    """
    List all services.
    """
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    """

    POST request: 

    elif request.method == 'POST':
        serializer = ServiceSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """

@api_view(['GET'])
def service_detail(request, pk):
    global Service
    """
    Get a specific service.
    """
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    """
    
    PUT and DELETE requests:

    elif request.method == 'PUT':
        serializer = ServiceSerializer(service, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    """

#Guest api functions here:

@api_view(['GET'])
def guest_list(request):
    global Guest
    """
    List all guests.
    """
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)

    """

    POST request: 

    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """

@api_view(['GET'])
def guest_detail(request, pk):
    global Guest
    """
    Get a specific guest.
    """
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    """
    
    PUT and DELETE requests:

    elif request.method == 'PUT':
        serializer = GuestSerializer(guest, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    """

#GuestPass api functions here:

@api_view(['GET'])
def guestpass_list(request):
    global GuestPass
    """
    List all guestpasses.
    """
    if request.method == 'GET':
        guestpasses = GuestPass.objects.all()
        serializer = GuestPassSerializer(guestpasses, many=True)
        return Response(serializer.data)

    """

    POST request: 

    elif request.method == 'POST':
        serializer = GuestPassSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """

@api_view(['GET'])
def guestpass_detail(request, pk):
    global GuestPass
    """
    Get a specific guestpass.
    """
    try:
        guestpass = GuestPass.objects.get(pk=pk)
    except GuestPass.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GuestPassSerializer(guestpass)
        return Response(serializer.data)

    """
    
    PUT and DELETE requests:

    elif request.method == 'PUT':
        serializer = GuestPassSerializer(guestpass, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        guestpass.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    """

#PersonalBill api functions here:

@api_view(['GET'])
def personalbill_list(request):
    global PersonalBill
    """
    List all personalbills.
    """
    if request.method == 'GET':
        personalbills = PersonalBill.objects.all()
        serializer = PersonalBillSerializer(personalbills, many=True)
        return Response(serializer.data)

    """

    POST request: 

    elif request.method == 'POST':
        serializer = PersonalBillSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
@api_view(['GET'])
def personalbill_detail(request, pk):
    global PersonalBill
    """
    Get a specific personalbill.
    """
    try:
        personalbill = PersonalBill.objects.get(pk=pk)
    except PersonalBill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonalBillSerializer(personalbill)
        return Response(serializer.data)

    """
    
    PUT and DELETE requests:

    elif request.method == 'PUT':
        serializer = PersonalBillSerializer(personalbill, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        personalbill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    """

#Person api functions here:

@api_view(['GET'])
def person_list(request):
    global Person
    """
    List all persons.
    """
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    """

    POST request: 

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
@api_view(['GET'])
def person_detail(request, pk):
    global Person
    """
    Get a specific person.
    """
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    """
    
    PUT and DELETE requests:

    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    """
