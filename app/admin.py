from django.contrib import admin
from .models import Company, Department, CompanyDepartment, User, Employee, Admin, DepartmentAdmin, Ticket, Comment, NotificationLog


admin.site.register(Company)
admin.site.register(Department)
admin.site.register(CompanyDepartment)
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Admin)
admin.site.register(DepartmentAdmin)
admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(NotificationLog)
