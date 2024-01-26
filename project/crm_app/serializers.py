import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *






class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("company_name", "phone", "email", "address", "client_status")


class SupplyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplyer
        fields = ("company_name", "phone", "email", "address", "supplyer_status")

class SdelkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sdelka
        fields = ("number", "description", "client" , "supplyer_1", "debitorka1", "status_sdelka")

