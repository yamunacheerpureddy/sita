from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
class Employee(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer