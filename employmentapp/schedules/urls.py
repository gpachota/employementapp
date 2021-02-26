from django.urls import path
from rest_framework.routers import SimpleRouter

from employmentapp.schedules.views import CompanyViewSet, PositionViewSet, EmployeeViewSet

router = SimpleRouter()

router.register('companies', CompanyViewSet, basename='companies')
router.register('positions', PositionViewSet, basename='positions')
router.register('employees', EmployeeViewSet, basename='employees')

urlpatterns = router.urls
