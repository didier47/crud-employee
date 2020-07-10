import uuid

from cassandra.cqlengine import columns
from django_cassandra.common.models import AuditoryModel
from django_cassandra.common.utilities import Enums


class EmployeeModel(AuditoryModel):
    _table_name = "employee"
    empl_id = columns.UUID(required=True, primary_key=True, default=uuid.uuid4)
    empl_first_name = columns.Text(required=True)
    empl_last_name = columns.Text(required=True)
    empl_identification = columns.Text(required=True)
    empl_birth_date = columns.DateTime(required=True)
    empl_address = columns.Text(required=False)
    empl_family_members = columns.Integer(required=True)
    empl_status = columns.Text(required=True, default=Enums.ACTIVO)

    class Meta:
        get_pk_field = 'empl_id'
