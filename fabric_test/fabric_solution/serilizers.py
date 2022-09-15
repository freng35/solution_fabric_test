from rest_framework import serializers
from fabric_solution.models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id', 'phone_number', 'operator_code', 'tag', 'time_zone']

    def create(self, validated_data):
        return Client.objects.create(**validated_data)


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = ['mail_id', 'date_start', 'text', 'filter', 'date_end']

    def create(self, validated_data):
        return Mail.objects.create(**validated_data)



