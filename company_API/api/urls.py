from django.contrib import admin
from django.urls import path,include
from api.views import companyViewSet,employeeViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies',companyViewSet)
router.register(r'employees',employeeViewSet)

urlpatterns=[
    path('',include(router.urls))
]