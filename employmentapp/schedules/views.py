from django.utils import timezone
from rest_framework import viewsets

from employmentapp.schedules import models
from employmentapp.schedules.models import Company, Position, Employee, Event
from employmentapp.schedules.serializers import CompanySerializer, PositionSerializer, EmployeeSerializer, \
    EventSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer

    def get_queryset(self):
        # return Company.objects.filter(user=self.request.user).all()
        return Company.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class PositionViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsTestUser,)
    serializer_class = PositionSerializer

    def get_queryset(self):
        # return Position.objects.filter(user=self.request.user).all()
        return Position.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(employee__user=self.request.user)

    def perform_create(self, serializer):
        employee_user = models.Employee.objects.get(user=self.request.user.id)
        serializer.save(created_at=timezone.now(), employee=employee_user)
