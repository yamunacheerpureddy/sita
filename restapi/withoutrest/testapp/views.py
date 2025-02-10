from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def emp_data_view(request):
    emp_data = {'eno': 101, 'ename': 'Sunny', 'esal': 12000, 'eaddr': 'Mumbai'}
    resp = f"<h1>Employee Number: {emp_data['eno']}<br>Employee Name: {emp_data['ename']}<br>Employee Salary: {emp_data['esal']}<br>Employee Address: {emp_data['eaddr']}</h1>"
    return HttpResponse(resp)
import json
def emp_data_jsonview(request):
    emp_data ={
    'eno' : 102,
    'ename' : 'Bunny',
    'esal' : 15000,
    'eaddr' : 'Hyd'
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data)
from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data ={
    'eno' : 103,
    'ename' : 'Vinny',
    'esal' : 18000,
    'eaddr' : 'Vja'
    }
    return JsonResponse(emp_data)

from django.views.generic import View
class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        emp_data ={
        'eno' : 104,
        'ename' : 'Radhika',
        'esal' : 22000,
        'eaddr' : 'Chennai'
        }
        return JsonResponse(emp_data)