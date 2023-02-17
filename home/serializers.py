from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
    def create(self,validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])  
        user.save()
        return user  
class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'
        
    def validate(self, data):
         if data['age']<18:
          raise serializers.ValidationError({"error":"age can't be less than 18"})   
         res = any(chr.isdigit() for chr in data['name'])
         if res:
             raise serializers.ValidationError({"error":"name can't contain any digit"})
         return data
class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class bookserializer(serializers.ModelSerializer):
     category=categoryserializer()
     class Meta:
        model=book
        fields='__all__'