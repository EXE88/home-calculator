from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProjectInputs
from .serializers import ProjectInputsSerializer,ProjectReviewSerializer
from rest_framework import permissions
from price.models import Material
from .city_choice_options import city_choises

class Calculate:
    def calculate_brick(self,pk):
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
        quantity_of_brick_for_ceiling_in_one_floor = ((home_length*100)/brick_length)*((home_width*100)/brick_length)
        quantity_of_brick_for_ceiling_in_all_floors = quantity_of_brick_for_ceiling_in_one_floor*obj.floor
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
                'one layer':{
                    'north wall of one floor':quantity_of_brick_in_north_and_south_wall_for_one_floor,
                    'south wall of one floor':quantity_of_brick_in_north_and_south_wall_for_one_floor,
                    'west wall of one floor':quantity_of_brick_in_west_and_east_wall_for_one_floor,
                    'east wall of one floor':quantity_of_brick_in_west_and_east_wall_for_one_floor,
                    'ceiling of one floor':quantity_of_brick_for_ceiling_in_one_floor
                },
                'two layer':{
                    'north wall of one floor':quantity_of_brick_in_north_and_south_wall_for_one_floor*2,
                    'south wall of one floor':quantity_of_brick_in_north_and_south_wall_for_one_floor*2,
                    'west wall of one floor':quantity_of_brick_in_west_and_east_wall_for_one_floor*2,
                    'east wall of one floor':quantity_of_brick_in_west_and_east_wall_for_one_floor*2,
                    'ceiling of one floor':quantity_of_brick_for_ceiling_in_one_floor  
                }
            },
            'quantity of brick for all floors':{
                'one layer':{
                    'north wall of the entire building':quantity_of_brick_in_north_and_south_wall_for_all_floors,
                    'south wall of the entire building':quantity_of_brick_in_north_and_south_wall_for_all_floors,
                    'west wall of the entire building':quantity_of_brick_in_west_and_east_wall_for_all_floors,
                    'east wall of the entire building':quantity_of_brick_in_west_and_east_wall_for_all_floors,
                    'ceiling of entire building':quantity_of_brick_for_ceiling_in_all_floors
                },
                'two layer':{
                    'north wall of the entire building':quantity_of_brick_in_north_and_south_wall_for_all_floors*2,
                    'south wall of the entire building':quantity_of_brick_in_north_and_south_wall_for_all_floors*2,
                    'west wall of the entire building':quantity_of_brick_in_west_and_east_wall_for_all_floors*2,
                    'east wall of the entire building':quantity_of_brick_in_west_and_east_wall_for_all_floors*2,
                    'ceiling of entire building':quantity_of_brick_for_ceiling_in_all_floors  
                }
            },
            'types of brick':list_of_brick_objects,
            'default of calculate':list_of_brick_objects[0],
            'costs':{
                'for one floor':{
                    'one layer':{
                        'north wall':float(quantity_of_brick_in_north_and_south_wall_for_one_floor)*float(current_price),
                        'south wall':float(quantity_of_brick_in_north_and_south_wall_for_one_floor)*float(current_price),
                        'west wall':float(quantity_of_brick_in_west_and_east_wall_for_one_floor)*float(current_price),
                        'east wall':float(quantity_of_brick_in_west_and_east_wall_for_one_floor)*float(current_price),
                        'ceiling':float(quantity_of_brick_for_ceiling_in_one_floor)*float(current_price)
                    },
                    'two layer':{
                        'north wall':(float(quantity_of_brick_in_north_and_south_wall_for_one_floor)*float(current_price))*2,
                        'south wall':(float(quantity_of_brick_in_north_and_south_wall_for_one_floor)*float(current_price))*2,
                        'west wall':(float(quantity_of_brick_in_west_and_east_wall_for_one_floor)*float(current_price))*2,
                        'east wall':(float(quantity_of_brick_in_west_and_east_wall_for_one_floor)*float(current_price))*2,
                        'ceiling':float(quantity_of_brick_for_ceiling_in_one_floor)*float(current_price) 
                    }
                },
                'for all floors':{
                    'one layer':{
                        'north wall':float(quantity_of_brick_in_north_and_south_wall_for_all_floors)*float(current_price),
                        'south wall':float(quantity_of_brick_in_north_and_south_wall_for_all_floors)*float(current_price),
                        'west wall':float(quantity_of_brick_in_west_and_east_wall_for_all_floors)*float(current_price),
                        'east wall':float(quantity_of_brick_in_west_and_east_wall_for_all_floors)*float(current_price),
                        'ceiling':float(quantity_of_brick_for_ceiling_in_all_floors)*float(current_price)
                    },
                    'two layer':{
                        'north wall':(float(quantity_of_brick_in_north_and_south_wall_for_all_floors)*float(current_price))*2,
                        'south wall':(float(quantity_of_brick_in_north_and_south_wall_for_all_floors)*float(current_price))*2,
                        'west wall':(float(quantity_of_brick_in_west_and_east_wall_for_all_floors)*float(current_price))*2,
                        'east wall':(float(quantity_of_brick_in_west_and_east_wall_for_all_floors)*float(current_price))*2,
                        'ceiling':float(quantity_of_brick_for_ceiling_in_all_floors)*float(current_price)
                    }
                }
            }
        }
        return data
    def calculate_cement(self,pk,data):
        cement_standard_size = 0.05
        data = data['needed material']['brick']
        one_floor_all_walls = data['quantity of brick for one floor']['one layer']
        north_wall_one_floor = data['quantity of brick for one floor']['one layer']['north wall of one floor']
        south_wall_one_floor = data['quantity of brick for one floor']['one layer']['south wall of one floor']
        west_wall_one_floor = data['quantity of brick for one floor']['one layer']['west wall of one floor']
        east_wall_one_floor = data['quantity of brick for one floor']['one layer']['east wall of one floor']
        ceiling_one_floor = data['quantity of brick for one floor']['one layer']['ceiling of one floor']
        data = {
            'cement':{
                'one floor':{
                    'one layer':{
                        'all':{
                            'north wall need cement (kg)':(north_wall_one_floor*cement_standard_size),
                            'south wall need cement (kg)':(south_wall_one_floor*cement_standard_size),
                            'west wall need cement (kg)':(west_wall_one_floor*cement_standard_size),
                            'east wall need cement (kg)':(east_wall_one_floor*cement_standard_size),
                            'ceiling need cement (kg)':(ceiling_one_floor*cement_standard_size),
                        },
                        'total':{
                            'total cement need (kg)':(one_floor_all_walls*cement_standard_size)
                        }
                    },
                    'two layer':{
                        'all':{
                            'north wall need cement (kg)':(north_wall_one_floor*cement_standard_size)*2,
                            'south wall need cement (kg)':(south_wall_one_floor*cement_standard_size)*2,
                            'west wall need cement (kg)':(west_wall_one_floor*cement_standard_size)*2,
                            'east wall need cement (kg)':(east_wall_one_floor*cement_standard_size)*2,
                            'ceiling need cement (kg)':(ceiling_one_floor*cement_standard_size),
                        },
                        'total':{
                            'total cement need (kg)':(one_floor_all_walls*cement_standard_size)*2
                        } 
                    }
                },
                'all floors':{
                    
                }
            }
        }
        

class CreateNewProject(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return ProjectInputs.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        serializer = ProjectInputsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            project_details = serializer.data
            for city in city_choises:
                if city[0] == project_details['city']:
                    project_details['city']=city[1]
            data = {
                "project details":project_details,
                "needed material":{
                    'brick':Calculate.calculate_brick(self,pk=project_details['id'])
                }  
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
        
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectInputsSerializer(project)
        project_details = serializer.data
        for city in city_choises:
            if city[0] == project_details['city']:
                project_details['city']=city[1]
                data = {
                    "project details":project_details,  
                    "needed material":{
                        'brick':Calculate.calculate_brick(self,pk=pk)
                    }  
                }
                Calculate.calculate_cement(self,pk=pk,data=data)
                return Response(data,status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectInputsSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "project details":serializer.data
            }
            return Response(data,status=status.HTTP_200_OK)
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
            data = {
                "project details":serializer.data
            }
            return Response(data,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND) 