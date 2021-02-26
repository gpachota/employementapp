from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken import serializers

from employmentapp.schedules.models import Company, Position, Employee
from employmentapp.schedules.serializers import CompanySerializer, PositionSerializer, EmployeeSerializer


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
