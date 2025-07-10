from django.db import models

from employees.models import Employee

# Create your models here.
class JournalDefinition(models.Model):
    journal_name = models.CharField(max_length=100)

    def __str__(self):
        return self.journal_name


class Register(models.Model):
    journal_id = models.ForeignKey(JournalDefinition, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)



class Invoice(models.Model):
    register_id = models.ForeignKey(Register, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50)
    invoice_date = models.DateField(auto_now_add=True)
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_schedule_id = models.ForeignKey('PaymentSchedule', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.invoice_date}"
    

class PaymentSchedule(models.Model):
    invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    payment_due_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending')

    def __str__(self):
        return f"Payment Schedule for {self.invoice_id.invoice_number} - Due: {self.payment_due_date}"


class PaymentRecord(models.Model):
    invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    payment_schedule_id = models.ForeignKey(PaymentSchedule, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[('Cash', 'Cash'), ('Credit Card', 'Credit Card'), ('Bank Transfer', 'Bank Transfer')], default='Cash')
    payment_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    transaction_reference = models.CharField(max_length=100, blank=True, null=True)


class ThirdParty(models.Model):
    third_party_name = models.CharField(max_length=255)
    third_party_address = models.CharField(max_length=255)
    third_party_phone_number = models.CharField(max_length=20)
    third_party_email = models.EmailField(max_length=255, blank=True, null=True)
    third_party_country = models.CharField(max_length=255)
    third_party_city = models.CharField(max_length=255)
    third_party_postal_code = models.CharField(max_length=20)
    category_third_party_id = models.ForeignKey('CategoryThirdParty', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.third_party_name
    

class CategoryThirdParty(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name