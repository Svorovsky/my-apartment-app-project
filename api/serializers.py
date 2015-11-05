from rest_framework import serializers

from InfoPage.models import InfoUnit
from Delivery.models import DeliveryService
from News.models import NewsItem
from Services.models import Service
from GuestPass.models import Guest, GuestPass
from MyBills.models import Bill, PersonalBill
from UserProfile.models import Person

class InfoUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfoUnit
        fields = ('title', 'description', 'phone_number', 'email')

class DeliveryServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryService
        fields = ('title', 'description', 'logo', 'menu_file')

class NewsItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsItem
        fields = ('title', 'subtitle', 'content', 'image')

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('title', 'subtitle', 'price', 'service_company_name', 'service_company_phone')

class GuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guest
        fields = ('first_name', 'patronymic', 'last_name', 'car_id')

class GuestPassSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuestPass
        fields = ('person', 'guest', 'date')

class PersonalBillSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalBill
        fields = ('person', 'bill', 'monthly_bill', 'arrear')


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('phone_number', 'password', 'first_name', 'patronymic', 'last_name', 'apartment_number', 'car_id' )

