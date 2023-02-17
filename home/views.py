from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import * 
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

@api_view(['GET'])
def get_book(request):  
    book_objs=book.objects.all()
    
    serializer=bookserializer(book_objs,many=True)
    return Response({'status':200,'payload':serializer.data})

from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUser(APIView):
    
    def post(self,request):
        serializer=userserializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403 ,'errors':serializer.errors,'message':'something went wrong'})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({'status':200,'payload':serializer.data,'message':'you sent','refresh': str(refresh),
        'access': str(refresh.access_token),})
       

from rest_framework import generics
class studentgeneric(generics.ListAPIView,generics.CreateAPIView):
    queryset =student.objects.all()
    serializer_class =studentserializer

class studentgeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset =student.objects.all()
    serializer_class =studentserializer
    lookup_field='id'
class StudentAPI(APIView):
      authentication_classes = [JWTAuthentication]
      permission_classes = [IsAuthenticated]
      def get(self,request):
          student_objs=student.objects.all()
          serializer=studentserializer(student_objs,many=True)
          print(request.user)
          return Response({'status':200,'payload':serializer.data})
           
      def post(self,request):
          serializer=studentserializer(data=request.data)
          if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403 ,'errors':serializer.errors,'message':'something went wrong'})
          serializer.save()
          return Response({'status':200,'payload':serializer.data,'message':'you sent'})
      def put(self,request):
          pass
      def patch(self,request):
          try:
                student_obj=student.objects.get(id=request.data['id'])
                    
                serializer=studentserializer(student_obj,data=request.data,partial=True)
                if not serializer.is_valid():
                    print(serializer.errors)
                    return Response({'status':403 ,'errors':serializer.errors,'message':'something went wrong'})
                serializer.save()
                return Response({'status':200,'payload':serializer.data,'message':'your data is updated'})
          except Exception as e:
                return Response({'status':403,'message':'invalid id'})
      def delete(self,request):
          try:
            student_obj=student.objects.get(id=request.data['id'])
            student_obj.delete()    
            serializer=studentserializer(student_obj,data=request.data)
            return Response({'status':200,'message':'deleted'})
          except Exception as e:
           print(e)   
           return Response({'status':403,'message':'invalid id'})

# import pandas as pd
# from django.conf import settings
# import uuid
# class exportimportexcel(APIView):
#     def get(self,request):
#         student_objs=student.objects.all() 
#         serializer=studentserializer(student_objs,many=True)
#         df=pd.DataFrame(serializer.data)
#         print(df)
#         df.to_csv(f"public/static/excel/{uuid.uuid4()}.csv",encoding="UTF-8")
#         return Response({'status':200})






# @api_view(['GET'])
# def home(request):  
#     student_objs=student.objects.all()
    
#     serializer=studentserializer(student_objs,many=True)
#     return Response({'status':200,'payload':serializer.data})
# @api_view(['POST'])
# def post_student(request):
#      data=request.data
#      serializer=studentserializer(data=request.data)
#      if not serializer.is_valid():
#          print(serializer.errors)
#          return Response({'status':403 ,'errors':serializer.errors,'message':'something went wrong'})
#      serializer.save()
#      return Response({'status':200,'payload':serializer.data,'message':'you sent'})
# @api_view(['PUT'])
# def update_student(request,id):
#      try:
#         student_obj=student.objects.get(id=id)
            
#         serializer=studentserializer(student_obj,data=request.data)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status':403 ,'errors':serializer.errors,'message':'something went wrong'})
#         serializer.save()
#         return Response({'status':200,'payload':serializer.data,'message':'you sent'})
#      except Exception as e:
#         return Response({'status':403,'message':'invalid id'})
        