from django.forms import ModelForm
from app.models import Employee, Contact, MynumberCard


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ( 'employee' ,)



class MynumberCardForm(ModelForm):
    class Meta:
        model = MynumberCard
        fields = '__all__'
        exclude = ( 'employee' ,)
