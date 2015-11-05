from rest_framework import serializers

from InfoPage.models import InfoUnit


class InfoUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfoUnit
        fields = ('title', 'description', 'phone_number', 'email')
