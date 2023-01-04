from django.forms import ModelForm
from myapp.models import Students

class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'section', 'photo']