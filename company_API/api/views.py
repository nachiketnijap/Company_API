from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import companySerializer,employeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class companyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=companySerializer

    @action(detail=True,methods=['get'])
    def employees(self, request,pk=None):
        try:
            company =Company.objects.get(pk=pk) 
            emps=Employee.objects.filter(company=company)
            emps_serializer=employeeSerializer (emps, many=True, context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            return Response({
                'message':'company might not exists'
            })

        

class employeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=employeeSerializer