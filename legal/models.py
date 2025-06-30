from django.db import models



from employees.models import Employee


# Create your models here.
class Document(models.Model):
    document_name = models.CharField(max_length=255)
    document_date = models.DateField(auto_now_add=False)
    document_title = models.CharField(max_length=255)
    document_description = models.TextField(blank=True, null=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    affair_id = models.ForeignKey('Affair', on_delete=models.CASCADE, blank=True, null=True)    
    category_document_id = models.ForeignKey('CategoryDocument', on_delete=models.CASCADE, blank=True, null=True)
    document_file = models.FileField(upload_to='documents/', blank=True, null=True)
    
    def __str__(self):
        return self.document_name

class Affair(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    affair_name = models.CharField(max_length=255)

class CategoryAffair(models.Model):
    affair_id = models.ForeignKey(Affair, on_delete=models.CASCADE)
    cat_aff_name = models.CharField(max_length=255)


class CategoryDocument(models.Model):
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    cat_doc_name = models.CharField(max_length=255)