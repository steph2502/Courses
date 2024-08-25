from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Courses
from .serializers import CoursesSerializer

@api_view(['GET','POST'])
def course_list(request):
    if request.method == 'GET':
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many= True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CoursesSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def course_detail(request,id):
    try:
        course = Courses.objects.get(pk=id)
    except Courses.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CoursesSerializer(course)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CoursesSerializer(course,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        course.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        

        
