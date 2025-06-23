from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.conf import settings 

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    domain = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return self.name
    

class Department(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name
    

class CompanyDepartment(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='departments_company')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_departments')

    def __str__(self):
        return f"{self.department.name} - {self.company.name}"


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'employee')


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (employee)"

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'admin')


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (admin)"
    

                                       
class DepartmentAdmin(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'admin_departments')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name= 'department_admins')



    def __str__(self):
        return f"{self.admin.first_name} {self.admin.last_name} - {self.admin.role} (admin of {self.department.name})"  
    

class Ticket(models.Model):
    ISSUE_CHOICES = [
        ('network', 'Network'),
        ('hardware', 'Hardware'), 
        ('software', 'Software'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('open', 'Open'),   
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    issue_type = models.CharField(max_length=50, choices=ISSUE_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='open')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='low')
    image = models.ImageField(upload_to='ticket_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    Date_Resolved = models.DateTimeField(null=True, blank=True)

    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='submitted_tickets')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='tickets')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name= 'tickets')

    def __str__(self):
        return f"Ticket #{self.id} - {self.title}"


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"comment by {self.user.email} on Ticket #{self.ticket.id}"
    

class NotificationLog(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name= 'notification')
    recipient_email = models.EmailField()
    notification_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Notification for {self.recipient_email} on Ticket #{self.ticket.id}"
    
