from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

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
    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def create(self, validate_data):
        user = User.objects.create(username = validate_data['username'])
        user.set_password(validate_data['password'])
        user.save()
        return user

# class CategorySerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Category
#         fields = '__all__'
        
# class BookSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
    
#     class Meta:
#         model = Book
#         fields = '__all__'
       # depth = 1
    
    
    
     
        # if data['name']:
        #     for n in data['name']:
        #         if n.isdigit():
        #             raise serializers.ValidationError({'error': 'name cannot be numeric'})