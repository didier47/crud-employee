import uuid

from django_cassandra.common.serializers import AuditorySerializer
from django_cassandra.common.utilities import Enums, Constants
from rest_framework import serializers

from employee.models import EmployeeModel


class EmployeeSerializer(AuditorySerializer):
    empl_id = serializers.UUIDField(read_only=True, default=uuid.uuid4)
    empl_first_name = serializers.CharField(required=True)
    empl_last_name = serializers.CharField(required=True)
    empl_identification = serializers.CharField(required=True)
    empl_birth_date = serializers.DateTimeField(required=True, format=Constants.FORMAT_DATE_TIME)
    empl_address = serializers.CharField(required=False)
    empl_family_members = serializers.IntegerField(required=True)
    empl_status = serializers.ChoiceField(required=False, choices=Enums.LIST_STATUS)

    class Meta:
        model = EmployeeModel
        fields = '__all__'
