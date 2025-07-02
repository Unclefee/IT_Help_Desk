from rest_framework import serializers
from .models import Company, Department, CompanyDepartment, User, Ticket, Comment, NotificationLog


class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = '__all__' 

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = '__all__'

class CompanyDepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = CompanyDepartment
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    exclude = ['password']

class TicketSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ticket
    fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'

class NotificationLogSerializer(serializers.ModelSerializer):
  class Meta:
    model = NotificationLog
    fields = '__all__'
    
