from rest_framework import serializers
from .models import ProjectInputs

class ProjectInputsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInputs
        fields = '__all__'
        
        
class ProjectReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInputs
        fields = ['created','title','city','area','floor']