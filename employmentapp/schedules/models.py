from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from employmentapp.schedules.constants import EventTypeE, PermissionTypeE


class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # permissions =

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    permission_type = models.SmallIntegerField(
        choices=[(permission_type.value, permission_type.name) for permission_type in PermissionTypeE], default=5)
    holiday_days_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_employee(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.employee.save()


class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee_id")
    event_type = models.SmallIntegerField(
        choices=[(event_type.value, event_type.name) for event_type in EventTypeE]
    )
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    created_at = models.DateTimeField()
