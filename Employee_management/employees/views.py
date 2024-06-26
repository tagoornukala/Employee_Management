from django.shortcuts import render,get_object_or_404,redirect
from .models import Employee,AddressDetails,Qualification,WorkExperience,Project
from .forms import EmployeeForm,AddressDetailsFormSet,QualificationFormSet,WorkExperienceFormSet,ProjectFormSet
from django.http import JsonResponse
# Create your views here.


def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=Employee())
        address_formset = AddressDetailsFormSet(request.POST, instance=Employee())
        work_experience_formset = WorkExperienceFormSet(request.POST, instance=Employee())
        qualification_formset = QualificationFormSet(request.POST, instance=Employee())
        project_formset = ProjectFormSet(request.POST, instance=Employee())

        if form.is_valid() and address_formset.is_valid() and work_experience_formset.is_valid() and qualification_formset.is_valid() and project_formset.is_valid():
            employee = form.save()
            address_formset.instance = employee
            address_formset.save()
            work_experience_formset.instance = employee
            work_experience_formset.save()
            qualification_formset.instance = employee
            qualification_formset.save()
            project_formset.instance = employee
            project_formset.save()
            return JsonResponse({'success':True,'employee_id':employee.id})
        else:
            errors = {
                'form_errors':form.errors,
                'address_errors' : address_formset.errors,
                'work_experience_errors' : work_experience_formset.errors,
                'qualification_errors' : qualification_formset.errors,
                'project_errors' : project_formset.errors
            }
            return JsonResponse({'success':False,'errors':errors}, status=400)
        
    else:
        form = EmployeeForm()
        address_formset = AddressDetailsFormSet(instance=Employee())
        work_experience_formset = WorkExperienceFormSet(instance=Employee())
        qualification_formset = QualificationFormSet(instance=Employee())
        project_formset = ProjectFormSet(instance=Employee())

    return render(request,'create_employee.html',{
        'form' : form,
        'address_formset' : address_formset,
        'work_experience_formset' : work_experience_formset,
        'qualification_formset' : qualification_formset,
        'project_formset' : project_formset
    })


def edit_employee(request,employee_id):
    employee = get_object_or_404(Employee,pk=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        address_formset = AddressDetailsFormSet(request.POST, instance=employee)
        work_experience_formset = WorkExperienceFormSet(request.POST, instance=employee)
        qualification_formset = QualificationFormSet(request.POST, instance=employee)
        project_formset = ProjectFormSet(request.POST, instance=employee)

        if form.is_valid() and address_formset.is_valid() and work_experience_formset.is_valid() and qualification_formset.is_valid() and project_formset.is_valid():
            form.save()
            address_formset.save()
            work_experience_formset.save()
            qualification_formset.save()
            project_formset.save()

            return JsonResponse({'success':True,'employee_id':employee_id})
        else:
            errors = {
                'form_errors':form.errors,
                'address_errors' : address_formset.errors,
                'work_experience_errors' : work_experience_formset.errors,
                'qualification_errors' : qualification_formset.errors,
                'project_errors' : project_formset.errors
            }
            return JsonResponse({'success':False,'errors':errors}, status=400)
        
    else:
        form = EmployeeForm(instance=employee)
        address_formset = AddressDetailsFormSet(instance=employee)
        work_experience_formset = WorkExperienceFormSet(instance=employee)
        qualification_formset = QualificationFormSet(instance=employee)
        project_formset = ProjectFormSet(instance=employee)

    return render(request,'edit_employee.html',{
        'form' : form,
        'address_formset' : address_formset,
        'work_experience_formset' : work_experience_formset,
        'qualification_formset' : qualification_formset,
        'project_formset' : project_formset,
        'employee' : employee
    })

 
