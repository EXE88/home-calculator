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
        all_brick_objects = Material.objects.filter(name__icontains='آجر')
        defult_calculate_object = Material.objects.filter(name__icontains='آجر فشاری در ابعاد 5*10*20')
        list_of_objects = []
        list_of_defult_objects = []
        
        for object in all_brick_objects:
            object_details = (object.name,object.brand,object.unit,object.price,object.last_price)
            list_of_objects.append(object_details)
        for object in defult_calculate_object:
            object_details = (object.name,object.brand,object.unit,object.price,object.last_price)
            list_of_defult_objects.append(object_details)
            
        current_price = list_of_objects[0][3].replace('تومان','')
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
            'types of brick':list_of_objects,
            'default of calculate':list_of_defult_objects,
            'costs':{
                'for one floor':{
                    'one layer':{
                        'north wall (تومان)':float(quantity_of_brick_in_north_and_south_wall_for_one_floor)*float(current_price),
                        'south wall (تومان)':float(quantity_of_brick_in_north_and_south_wall_for_one_floor)*float(current_price),
                        'west wall (تومان)':float(quantity_of_brick_in_west_and_east_wall_for_one_floor)*float(current_price),
                        'east wall (تومان)':float(quantity_of_brick_in_west_and_east_wall_for_one_floor)*float(current_price),
                        'ceiling (تومان)':float(quantity_of_brick_for_ceiling_in_one_floor)*float(current_price)
                    },
                    'two layer':{
                        'north wall (تومان)':(float(quantity_of_brick_in_north_and_south_wall_for_one_floor)*float(current_price))*2,
                        'south wall (تومان)':(float(quantity_of_brick_in_north_and_south_wall_for_one_floor)*float(current_price))*2,
                        'west wall (تومان)':(float(quantity_of_brick_in_west_and_east_wall_for_one_floor)*float(current_price))*2,
                        'east wall (تومان)':(float(quantity_of_brick_in_west_and_east_wall_for_one_floor)*float(current_price))*2,
                        'ceiling (تومان)':float(quantity_of_brick_for_ceiling_in_one_floor)*float(current_price) 
                    }
                },
                'for all floors':{
                    'one layer':{
                        'north wall (تومان)':float(quantity_of_brick_in_north_and_south_wall_for_all_floors)*float(current_price),
                        'south wall (تومان)':float(quantity_of_brick_in_north_and_south_wall_for_all_floors)*float(current_price),
                        'west wall (تومان)':float(quantity_of_brick_in_west_and_east_wall_for_all_floors)*float(current_price),
                        'east wall (تومان)':float(quantity_of_brick_in_west_and_east_wall_for_all_floors)*float(current_price),
                        'ceiling (تومان)':float(quantity_of_brick_for_ceiling_in_all_floors)*float(current_price)
                    },
                    'two layer':{
                        'north wall (تومان)':(float(quantity_of_brick_in_north_and_south_wall_for_all_floors)*float(current_price))*2,
                        'south wall (تومان)':(float(quantity_of_brick_in_north_and_south_wall_for_all_floors)*float(current_price))*2,
                        'west wall (تومان)':(float(quantity_of_brick_in_west_and_east_wall_for_all_floors)*float(current_price))*2,
                        'east wall (تومان)':(float(quantity_of_brick_in_west_and_east_wall_for_all_floors)*float(current_price))*2,
                        'ceiling (تومان)':float(quantity_of_brick_for_ceiling_in_all_floors)*float(current_price)
                    }
                }
            }
        }
        return data
    def calculate_cement(self,pk,data):
        obj = self.get_object(pk=pk)
        floors = obj.floor
        cement_standard_size = 0.05
        north_wall_one_floor = data['quantity of brick for one floor']['one layer']['north wall of one floor']
        south_wall_one_floor = data['quantity of brick for one floor']['one layer']['south wall of one floor']
        west_wall_one_floor = data['quantity of brick for one floor']['one layer']['west wall of one floor']
        east_wall_one_floor = data['quantity of brick for one floor']['one layer']['east wall of one floor']
        ceiling_one_floor = data['quantity of brick for one floor']['one layer']['ceiling of one floor']
        one_floor_all_walls = north_wall_one_floor+south_wall_one_floor+west_wall_one_floor+east_wall_one_floor+ceiling_one_floor
        all_cement_objects = Material.objects.filter(name__icontains='سیمان')
        defult_calculate_object = Material.objects.filter(name__icontains='سیمان پرتلند تیپ 2')
        list_of_objects = []
        list_of_defult_calculate_object = []
        
        for object in all_cement_objects:
            object_detials = (object.name,object.brand,object.unit,object.price,object.last_price)
            list_of_objects.append(object_detials)
        for object in defult_calculate_object:
            object_detials = (object.name,object.brand,object.unit,object.price,object.last_price)
            list_of_defult_calculate_object.append(object_detials)
            
        current_price = list_of_objects[0][3].replace('تومان','')
        current_price = current_price.replace(',','')   
            
        data = {
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
                        'total cement need (kg)':(((north_wall_one_floor+south_wall_one_floor+west_wall_one_floor+east_wall_one_floor)*cement_standard_size)*2)+(ceiling_one_floor*cement_standard_size)
                    } 
                }
            },
            'all floors':{
               'one layer':{
                   'all':{
                        'north wall need cement (kg)':(north_wall_one_floor*cement_standard_size)*floors,
                        'south wall need cement (kg)':(south_wall_one_floor*cement_standard_size)*floors,
                        'west wall need cement (kg)':(west_wall_one_floor*cement_standard_size)*floors,
                        'east wall need cement (kg)':(east_wall_one_floor*cement_standard_size)*floors,
                        'ceiling need cement (kg)':(ceiling_one_floor*cement_standard_size)*floors,
                   },
                   'total':{
                       'total cement need (kg)':(one_floor_all_walls*cement_standard_size)*floors
                   }
               },
               'two layer':{
                   'all':{
                        'north wall need cement (kg)':((north_wall_one_floor*cement_standard_size)*2)*floors,
                        'south wall need cement (kg)':((south_wall_one_floor*cement_standard_size)*2)*floors,
                        'west wall need cement (kg)':((west_wall_one_floor*cement_standard_size)*2)*floors,
                        'east wall need cement (kg)':((east_wall_one_floor*cement_standard_size)*2)*floors,
                        'ceiling need cement (kg)':(ceiling_one_floor*cement_standard_size)*floors,
                   },
                   'total':{
                       'total cement need (kg)':((((north_wall_one_floor+south_wall_one_floor+west_wall_one_floor+east_wall_one_floor)*cement_standard_size)*2)+(ceiling_one_floor*cement_standard_size))*floors
                   }
                }
            },
            'types of cement':list_of_objects,
            'defult cement for calcualte':list_of_defult_calculate_object,
            'costs':{
                'for one floor':{
                    'one layer':{
                        'all':{
                            'north wall (تومان)':float((north_wall_one_floor*cement_standard_size))*float(current_price),
                            'south wall (تومان)':float((south_wall_one_floor*cement_standard_size))*float(current_price),
                            'west wall (تومان)':float((west_wall_one_floor*cement_standard_size))*float(current_price),
                            'east wall (تومان)':float((east_wall_one_floor*cement_standard_size))*float(current_price),
                            'ceiling (تومان)':float((ceiling_one_floor*cement_standard_size))*float(current_price),
                        },
                        'total':{
                            'total price (تومان)':float((one_floor_all_walls*cement_standard_size))*float(current_price)
                        }
                    },
                    'two layer':{
                        'all':{
                            'north wall (تومان)':float((north_wall_one_floor*cement_standard_size)*2)*float(current_price),
                            'south wall (تومان)':float((south_wall_one_floor*cement_standard_size)*2)*float(current_price),
                            'west wall (تومان)':float((west_wall_one_floor*cement_standard_size)*2)*float(current_price),
                            'east wall (تومان)':float((east_wall_one_floor*cement_standard_size)*2)*float(current_price),
                            'ceiling (تومان)':float((ceiling_one_floor*cement_standard_size))*float(current_price),
                        },
                        'total':{
                            'total price (تومان)':float((((north_wall_one_floor+south_wall_one_floor+west_wall_one_floor+east_wall_one_floor)*cement_standard_size)*2)+(ceiling_one_floor*cement_standard_size))*float(current_price)
                        }
                    }
                },
                'for all floors':{
                    'one layer':{
                        'all':{
                            'north wall (تومان)':float((north_wall_one_floor*cement_standard_size)*floors)*float(current_price),
                            'south wall (تومان)':float((south_wall_one_floor*cement_standard_size)*floors)*float(current_price),
                            'west wall (تومان)':float((west_wall_one_floor*cement_standard_size)*floors)*float(current_price),
                            'east wall (تومان)':float((east_wall_one_floor*cement_standard_size)*floors)*float(current_price),
                            'ceiling (تومان)':float((ceiling_one_floor*cement_standard_size)*floors)*float(current_price),
                        },
                        'total':{
                            'total price (تومان)':float((one_floor_all_walls*cement_standard_size)*floors)*float(current_price)
                        }
                    },
                    'two layer':{
                        'all':{
                            'north wall (تومان)':float(((north_wall_one_floor*cement_standard_size)*2)*floors)*float(current_price),
                            'south wall (تومان)':float(((south_wall_one_floor*cement_standard_size)*2)*floors)*float(current_price),
                            'west wall (تومان)':float(((west_wall_one_floor*cement_standard_size)*2)*floors)*float(current_price),
                            'east wall (تومان)':float(((east_wall_one_floor*cement_standard_size)*2)*floors)*float(current_price),
                            'ceiling (تومان)':float((ceiling_one_floor*cement_standard_size)*floors)*float(current_price),
                        },
                        'total':{
                            'total price (تومان)':float(((((north_wall_one_floor+south_wall_one_floor+west_wall_one_floor+east_wall_one_floor)*cement_standard_size)*2)+(ceiling_one_floor*cement_standard_size))*floors)*float(current_price)
                        }
                    }
                }
            }
        }
        return data
        

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
                        'brick':Calculate.calculate_brick(self,pk=pk),
                        'cement':Calculate.calculate_cement(self,pk=pk,data=Calculate.calculate_brick(self,pk=pk))
                    }  
                }
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