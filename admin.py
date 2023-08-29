from django.contrib import admin
from service.models import Employee
from service.models import signup

# Register your models here.
class EmployeeDetail(admin.ModelAdmin):
    list_display=['Name', 'Email', 'Phone', 'Address']

class signupDetail(admin.ModelAdmin):
    list_display=['Name', 'Email', 'Phone', 'Password', 'Gender']


admin.site.register(Employee,EmployeeDetail)
admin.site.register(signup,signupDetail)
