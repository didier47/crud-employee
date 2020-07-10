from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from django_cassandra.common.filters import FilterSet, CustomDateTimeFilter
from django_cassandra.common.views import ModelViewSet
from rest_framework.filters import OrderingFilter

from employee.models import EmployeeModel
from employee.serializer import EmployeeSerializer


class EmployeeFilter(FilterSet):
    empl_id = filters.CharFilter(lookup_expr='eq')
    empl_first_name = filters.CharFilter(lookup_expr='eq')
    empl_last_name = filters.CharFilter(lookup_expr='eq')
    empl_identification = filters.CharFilter(lookup_expr='eq')
    empl_birth_date = CustomDateTimeFilter(field_name='empl_birth_date', lookup_expr='gte')
    empl_address = filters.CharFilter(lookup_expr='eq')
    empl_family_members = filters.NumberFilter(lookup_expr='eq')
    empl_status = filters.CharFilter(lookup_expr='eq')

    class Meta:
        model = EmployeeModel
        fields = ['empl_id', 'empl_first_name', 'empl_last_name', 'empl_identification', 'empl_birth_date',
                  'empl_address', 'empl_family_members', 'empl_status']


class EmployeeViewSet(ModelViewSet):
    queryset = EmployeeModel.objects
    serializer_class = EmployeeSerializer
    lookup_field = 'empl_id'
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EmployeeFilter
    ordering_fields = ['empl_first_name', 'empl_last_name', 'empl_identification', 'empl_birth_date', 'empl_address',
                       'empl_family_members']
