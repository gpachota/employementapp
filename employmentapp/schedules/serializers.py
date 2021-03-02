from django.contrib.auth.models import User
from rest_framework import serializers

from employmentapp.schedules.constants import EventTypeE
from employmentapp.schedules.models import Company, Position, Employee, Event


class CompanySerializer(serializers.ModelSerializer):

    def getOwnerName(self, obj):
        return obj.owner.username

    owner_name = serializers.SerializerMethodField("getOwnerName")

    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'description',
            'owner',
            'owner_name'
        )


class PositionSerializer(serializers.ModelSerializer):

    def getCompanyName(self, obj):
        return obj.company.name

    company_name = serializers.SerializerMethodField("getCompanyName")

    class Meta:
        model = Position
        fields = (
            'id',
            'name',
            'company',
            'company_name'

        )


class EmployeeSerializer(serializers.ModelSerializer):

    def getUsername(self, obj):
        return obj.user.username

    def getCompanyName(self, obj):
        return obj.company.name

    def getPositionName(self, obj):
        return obj.position.name

    username = serializers.SerializerMethodField("getUsername")
    company_name = serializers.SerializerMethodField("getCompanyName")
    position_name = serializers.SerializerMethodField("getPositionName")

    class Meta:
        model = Employee
        fields = (
            'id',
            'user',
            'username',
            'company',
            'company_name',
            'position',
            'position_name'
        )


class EventSerializer(serializers.ModelSerializer):

    def getEmployeeName(self, obj):
        return obj.employee.user.username

    def getEventTypeName(self, obj):
        return EventTypeE(obj.event_type).name

    def getCreatedAtDate(self, obj):
        return obj.created_at

    def getHoursCount(self, obj):
        return (obj.to_date - obj.from_date) / 3600

    employee_name = serializers.SerializerMethodField("getEmployeeName")
    event_type_name = serializers.SerializerMethodField("getEventTypeName")
    created_at_date = serializers.SerializerMethodField("getCreatedAtDate")
    hours_count = serializers.SerializerMethodField("getHoursCount")

    class Meta:
        model = Event
        fields = (
            'id',
            'employee_name',
            'event_type',
            'event_type_name',
            'created_at_date',
            'from_date',
            'to_date',
            'hours_count'
        )
