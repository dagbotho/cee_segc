from django.db import models

# Create your models here.
class EmployeeStatus(models.Model):
    status_name = models.CharField(max_length=255)


class CategoryPro(models.Model):
    name_cat_pro = models.CharField(max_length=255)


class Employee(models.Model):
    empl_status_id = models.ForeignKey(EmployeeStatus, on_delete=models.CASCADE)
    cat_pro_id = models.ForeignKey(CategoryPro, on_delete=models.CASCADE)
    empl_last_name = models.CharField(max_length=255)
    empl_first_name = models.CharField(max_length=255)
    empl_DOB = models.DateField(auto_now_add=False)
    empl_city_of_Birth = models.CharField(max_length=255)
    employee_ID_number = models.CharField(max_length=15)
    empl_ID_Place_of_origin = models.CharField(max_length=155)


class EmployeeFunction(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    empl_function_name = models.CharField(max_length=255)
    empl_function_description = models.TextField(blank=True, null=True)
    empl_function_date = models.DateField(auto_now_add=False)
    empl_function_time = models.TimeField(auto_now_add=False)

    def __str__(self):
        return f"{self.employee_id.empl_first_name} {self.employee_id.empl_last_name} - {self.empl_function_name}"
    

class EmployeeTask(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    empl_task_name = models.CharField(max_length=255)
    empl_task_description = models.TextField(blank=True, null=True)
    empl_task_date = models.DateField(auto_now_add=False)
    empl_task_time = models.TimeField(auto_now_add=False)

    def __str__(self):
        return f"{self.employee_id.empl_first_name} {self.employee_id.empl_last_name} - {self.empl_task_name}"


class Branch(models.Model):
    branch_name = models.CharField(max_length=255)
    branch_address = models.CharField(max_length=255)
    branch_phone_number = models.CharField(max_length=20)
    branch_email = models.EmailField(max_length=255, blank=True, null=True)
    branch_country = models.CharField(max_length=255)
    branch_city = models.CharField(max_length=255)
    branch_postal_code = models.CharField(max_length=20)



class Manage(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    manage_date = models.DateField(auto_now_add=False)
    manage_time = models.TimeField(auto_now_add=False)

    def __str__(self):
        return f"{self.employee_id.empl_first_name} {self.employee_id.empl_last_name} - {self.branch_id.branch_name}"
    

class ManageBy(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    manage_by_date = models.DateField(auto_now_add=False)
    manage_by_time = models.TimeField(auto_now_add=False)

    def __str__(self):
        return f"{self.employee_id.empl_first_name} {self.employee_id.empl_last_name}"
    





