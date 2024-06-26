from django import forms
from django.forms import inlineformset_factory
from .models import Employee,AddressDetails,WorkExperience,Qualification,Project

class AddressDetailsForm(forms.ModelForm):
    class Meta:
        model = AddressDetails
        fields = '__all__'

class WorkExperienceForm(forms.ModelForm):
    from_date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d'), input_formats=['%Y-%m-%d'])
    to_date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d'), input_formats=['%Y-%m-%d'])

    class Meta:
        model = WorkExperience
        fields = '__all__'

class QualificationsForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

AddressDetailsFormSet = inlineformset_factory(Employee, AddressDetails, form=AddressDetailsForm, extra=1, can_delete=True)
WorkExperienceFormSet = inlineformset_factory(Employee, WorkExperience, form=WorkExperienceForm, extra=1, can_delete=True)
QualificationFormSet = inlineformset_factory(Employee, Qualification, form=QualificationsForm, extra=1, can_delete=True)
ProjectFormSet = inlineformset_factory(Employee, Project, form=ProjectForm, extra=1, can_delete=True)

