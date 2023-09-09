from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProjectInputs
from .serializers import ProjectInputsSerializer,ProjectReviewSerializer
from rest_framework import permissions

class CreateNewProject(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = ProjectInputsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ProjectFullDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return ProjectInputs.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectInputsSerializer(project)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectInputsSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_200_OK)
    
class ProjectReview(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,pk):
        try:
            project = ProjectInputs.objects.get(pk=pk)
            serializer = ProjectReviewSerializer(project)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND) 