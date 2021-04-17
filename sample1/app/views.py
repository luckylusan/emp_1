from django.shortcuts import render
from .models import employee
from .serializers import employeeSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class EmploeeTable(APIView):

    def get(self,request):
        emp_obj =employee.objects.all()
        emp_serializer_obj = employeeSerializers(emp_obj,many=True)
        return Response(emp_serializer_obj.data)

    def post(self,request):
        serialize_object = employeeSerializers(data=request.data)
        if serialize_object.is_valid():
            serialize_object.save()
            return Response(serialize_object.data,status=status.HTTP_200_OK)
        return Response(serialize_object.errors,status=status.HTTP_400_BAD_REQUEST)

class EmployeeUpdate(APIView):

    def get_object(self,pk):
        emp_obj = self.get_object(pk)
        serialize_obj = employeeSerializers(emp_obj)

        try:
            return employee.objects.get(pk=pk)
        except employee.DoesNotExist:
            return Response(serialize_obj.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        emp_obj = self.get_object(pk)
        serialize_obj = employeeSerializers(emp_obj)
        return  Response(serialize_obj.data)

    def put(self,request,pk):
        emp_obj = self.get_object(pk)
        emp_serialize_obj = employeeSerializers(emp_obj,data=request.data)
        if emp_serialize_obj.is_valid():
            emp_serialize_obj.save()
            return Response(emp_serialize_obj,status=status.HTTP_200_OK)
        return Response(emp_serialize_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        emp_obj = self.get_object(pk)
        emp_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)