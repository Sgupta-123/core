from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=18)
    father_name=models.CharField(max_length=100)
    
class Category(models.Model):
    category_name=models.CharField(max_length=100)
class book(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    book_title=models.CharField(max_length=100)
class excelfileupload(models.Model):
    excel_file_upload=models.FileField(upload_to="excel")