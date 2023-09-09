from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .models import *
from .serializer import *

# Create your views here.

# @api_view(['GET'])
# def get_book(request):
#     book_objs = Book.objects.all()
#     serializer = BookSerializer(book_objs, many = True)
    
#     return Response({'status' : 200, 'payload': serializer.data})

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'error': serializer.errors , 'message': 'some error in information.'})
    
        serializer.save()
    
        user = User.objects.get(username = serializer.data['username'])    
        token_obj , _ = Token.objects.get_or_create(user=user)
        
        return Response({'status': 200, 'payload': serializer.data, 'token': str(token_obj), 'message': 'your data is submited !!'})


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#same from drf docum.

class StudentAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # permissions import kari h django restframework documentation
    
    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many= True)
        print(request.user)
        
        return Response({'status':200, 'payload': serializer.data})
    
    def post(self, request):
            data = request.data
            serializer = StudentSerializer(data = request.data)
    
    
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'error': serializer.errors , 'message': 'some error in information.'})
    
            serializer.save()
    
            return Response({'status': 200, 'payload': serializer.data, 'message': 'your data is submited !!'})

    def put(self, request):
        pass
    
    def patch(self, request):
        try:
            student_obj = Student.objects.get (id = request.data['id'])
            
            serializer = StudentSerializer(student_obj, data = request.data, partial = True)
            
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'error': serializer.errors, 'message': 'some error in information..'})
            
            serializer.save()

            return Response({'status': 200, 'payload': serializer.data, 'message': 'your data is submited !!'})
    
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'invalid id'})
    
    def delete(self, request):        
        try:
            # id= request.GET.get('id')   isme aage def() se id hatana pdega and /?id=3 pass kar sakte hai thunderclient mai 
            student_obj = Student.objects.get(id = id)
            student_obj.delete()
            return Response({'status':200, 'message': 'Deleted !!' })
    
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'invalid id'})
    






# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many= True)
    
#     return Response({'status':200, 'payload': serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serializer = StudentSerializer(data = request.data)
    
    
#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status': 403, 'error': serializer.errors , 'message': 'some error in information.'})
    
#     serializer.save()
    
#     return Response({'status': 200, 'payload': serializer.data, 'message': 'your data is submited !!'})

# @api_view(['PATCH'])
# def update_student(request, id):
#     try:
#         student_obj = Student.objects.get (id = id)
        
#         serializer = StudentSerializer(student_obj, data = request.data, partial = True)
        
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 403, 'error': serializer.errors, 'message': 'some error in information..'})
        
#         serializer.save()

#         return Response({'status': 200, 'payload': serializer.data, 'message': 'your data is submited !!'})
    
#     except Exception as e:
#         print(e)
#         return Response({'status': 403, 'message': 'invalid id'})
    
# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         # id= request.GET.get('id')   isme aage def() se id hatana pdega and /?id=3 pass kar sakte hai thunderclient mai 
#         student_obj = Student.objects.get(id = id)
#         student_obj.delete()
#         return Response({'status':200, 'message': 'Deleted !!' })
    
#     except Exception as e:
#         print(e)
#         return Response({'status': 403, 'message': 'invalid id'})
        
    

# serializer ek variable hai jisme hai query set mai data pass karte hai 
# and many = True isliye kara hai kyuki isme bulk mai data aata hai

#  data = request.data ---- se frontend ka data lete hai 

#@api_view(['POST'])
#def home(request):
   # return Response({'Status':200, 'message':'hello from django rest framework'})
   
   

#    if request.data['age'] < 18:
 #       return Response({'status': 403, 'message': 'age must be greater than 18"'})  



        
