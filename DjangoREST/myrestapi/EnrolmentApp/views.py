
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import student
from .serializers import studentserializer
from rest_framework import mixins
from rest_framework import generics
from django.http import Http404


from django.http import HttpResponse
import datetime

def current_datetime(request):                 #tried incuding the time on the app, but it doesnt reflect
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# Create your views here:

class studentlist(APIView):

    def get(self, request, format=None):
        student1 = student.objects.all()
        serializer = studentserializer(student1, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class studentdata(APIView):
    """
    Retrieve, update or delete student detaila
    """
    def get_object(self, pk):
        try:
            return student.objects.get(pk=pk)
        except student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student1 = self.get_object(pk)
        serializer = studentserializer(student1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student1 = self.get_object(pk)
        serializer = studentserializer(student1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student1 = self.get_object(pk)
        student1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



