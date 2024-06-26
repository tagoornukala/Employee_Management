from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return self.name
    
class AddressDetails(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='address_details')
    hno = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.employee.name}'s Address" 
    
class WorkExperience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='work_experience')
    company_name = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.employee.name}'s Work Experience"
    
class Qualification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='qualifications')
    qualification_name = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"{self.employee.name}'s Qualification"
    
class Project(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='project_photos/',blank=True,null=True)

    def __str__(self):
        return self.title