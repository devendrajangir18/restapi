from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import *
from .serializer import *

# Create your views here.

@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs, many= True)
    
    return Response({'status':200, 'payload': serializer.data})

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data = request.data)
    
    
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status': 403, 'error': serializer.errors , 'message': 'some error in information.'})
    
    serializer.save()
    
    return Response({'status': 200, 'payload': serializer.data, 'message': 'your data is submited !!'})
    

# serializer ek variable hai jisme hai query set mai data pass karte hai 
# and many = True isliye kara hai kyuki isme bulk mai data aata hai

#  data = request.data ---- se frontend ka data lete hai 

#@api_view(['POST'])
#def home(request):
   # return Response({'Status':200, 'message':'hello from django rest framework'})
   
   

#    if request.data['age'] < 18:
 #       return Response({'status': 403, 'message': 'age must be greater than 18"'})  



        
