from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProjectInputs
from .serializers import ProjectInputsSerializer,ProjectReviewSerializer
from rest_framework import permissions
from price.models import Material

class CreateNewProject(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = ProjectInputsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
            "project details":serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ProjectFullDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return ProjectInputs.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def calculate(self,pk):
        
        obj = self.get_object(pk=pk)
        home_length = obj.length
        home_width = obj.width
        home_height = 2.8
        
        brick_length = 20
        brick_width = 10
        brick_height = 5
        
        quantity_of_brick_in_north_and_south_wall_for_one_floor = ((home_length*100)/brick_length)*((home_height*100)/brick_height)
        quantity_of_brick_in_west_and_east_wall_for_one_floor = ((home_width*100)/brick_length)*((home_height*100)/brick_height)
        
        quantity_of_brick_in_north_and_south_wall_for_all_floors = quantity_of_brick_in_north_and_south_wall_for_one_floor*obj.floor
        quantity_of_brick_in_west_and_east_wall_for_all_floors = quantity_of_brick_in_west_and_east_wall_for_one_floor*obj.floor
        
        all_brick_objects = Material.objects.none()
        all_brick_objects |= Material.objects.filter(name__icontains='آجر')
        list_of_brick_objects = []
        for brick in all_brick_objects:
            object_details = (brick.name,brick.brand,brick.unit,brick.price,brick.last_price)
            list_of_brick_objects.append(object_details)
        current_price = list_of_brick_objects[0][3].replace('تومان','')
        current_price = current_price.replace(',','')
            
        data = {
            'quantity of brick for one floor':{
                'north wall of one floor':quantity_of_brick_in_north_and_south_wall_for_one_floor,
                'south wall of one floor':quantity_of_brick_in_north_and_south_wall_for_one_floor,
                'west wall of one floor':quantity_of_brick_in_west_and_east_wall_for_one_floor,
                'east wall of one floor':quantity_of_brick_in_west_and_east_wall_for_one_floor
            },
            'quantity of brick for all floors':{
                'north wall of the entire building':quantity_of_brick_in_north_and_south_wall_for_all_floors,
                'south wall of the entire building':quantity_of_brick_in_north_and_south_wall_for_all_floors,
                'west wall of the entire building':quantity_of_brick_in_west_and_east_wall_for_all_floors,
                'east wall of the entire building':quantity_of_brick_in_west_and_east_wall_for_all_floors,
            },
            'types of brick':list_of_brick_objects,
            'default of calculate':list_of_brick_objects[0],
            'costs':{
                'for one floor':{
                    'north wall':float(quantity_of_brick_in_north_and_south_wall_for_one_floor)*float(current_price),
                    'south wall':float(quantity_of_brick_in_north_and_south_wall_for_one_floor)*float(current_price),
                    'west wall':float(quantity_of_brick_in_west_and_east_wall_for_one_floor)*float(current_price),
                    'east wall':float(quantity_of_brick_in_west_and_east_wall_for_one_floor)*float(current_price)
                },
                'for all floors':{
                    'north wall':float(quantity_of_brick_in_north_and_south_wall_for_all_floors)*float(current_price),
                    'south wall':float(quantity_of_brick_in_north_and_south_wall_for_all_floors)*float(current_price),
                    'west wall':float(quantity_of_brick_in_west_and_east_wall_for_all_floors)*float(current_price),
                    'east wall':float(quantity_of_brick_in_west_and_east_wall_for_all_floors)*float(current_price) 
                }
            }
        }
        
        return data
        
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectInputsSerializer(project)
        data = {
            "project details":serializer.data,  
            "needed material":{
                'brick':self.calculate(pk=pk)
            }  
        }
        return Response(data,status=status.HTTP_200_OK)
    
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