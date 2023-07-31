from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        #fields = ['name', 'age'] #for some specific on=bjects
        #exclude = ['id']
        fields = '__all__'
        
    def validate(self, data):
        
        if data['age'] < 18 :
            raise serializers.ValidationError({'error' : 'Age cannot be less than 18'})
        
        
        return data