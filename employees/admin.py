from django.contrib import admin

from .models import Employee, EmployeeStatus, CategoryPro, EmployeeFunction, EmployeeTask, Branch

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'empl_first_name', 'empl_last_name']
    search_fields = ['empl_first_name', 'empl_last_name',]
    ordering = ['empl_last_name', 'empl_first_name']
    list_per_page = 20



@admin.register(EmployeeStatus)
class EmployeeStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_name']
    search_fields = ['status_name']
    ordering = ['status_name']
    list_per_page = 20


@admin.register(CategoryPro)
class CategoryProAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_cat_pro']
    search_fields = ['name_cat_pro']
    ordering = ['name_cat_pro']
    list_per_page = 20

@admin.register(EmployeeFunction)
class EmployeeFunctionAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_id', 'empl_function_name', 'empl_function_date', 'empl_function_time']
    search_fields = ['employee_id__empl_first_name', 'employee_id__empl_last_name', 'empl_function_name']
    list_filter = ['empl_function_date']
    ordering = ['empl_function_date', 'employee_id__empl_last_name']
    list_per_page = 20

@admin.register(EmployeeTask)
class EmployeeTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_id', 'empl_task_name', 'empl_task_date', 'empl_task_time']
    search_fields = ['employee_id__empl_first_name', 'employee_id__empl_last_name', 'empl_task_name']
    list_filter = ['empl_task_date']
    ordering = ['empl_task_date', 'employee_id__empl_last_name']
    list_per_page = 20


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'branch_name', 'branch_address', 'branch_phone_number', 'branch_email', 'branch_country', 'branch_city', 'branch_postal_code']
    search_fields = ['branch_name', 'branch_address', 'branch_email']
    list_filter = ['branch_country', 'branch_city']
    ordering = ['branch_name']
    list_per_page = 20