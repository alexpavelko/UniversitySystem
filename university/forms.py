from django import forms
from .models import *


class TeacherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['creation_date', ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 400px;'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 400px;'}),
            'email': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 400px;'}),
            'job_position': forms.Select(attrs={'class': 'form-select', 'style': 'width: 400px;'}, choices=JOB_POSITION_CHOICES),
        }


class SubjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 600px;'}),
            'teacher': forms.Select(attrs={'class': 'form-select', }, choices=JOB_POSITION_CHOICES),
            'group': forms.Select(attrs={'class': 'form-select', 'style': 'width: 600px;'}, choices=Group.objects.all),
        }


class GroupForm(forms.ModelForm):
    def init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 600px;'}),
            'course': forms.Select(attrs={'class': 'form-input', 'style': 'width: 100px;'}, choices=COURSE_CHOICES),
        }


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 400px;'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 400px;'}),
            'email': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 400px;'}),
            'ticket_number': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 400px;'}),
            'group': forms.Select(attrs={'class': 'form-input', 'style': 'width: 300px;'}, choices=Group.objects.all),
        }


class GradeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        student = kwargs.pop('student', None)
        super().__init__(*args, **kwargs)

        if student:
            self.fields['subject'].queryset = student.group.subjects

    class Meta:
        model = Grade
        fields = '__all__'
        exclude = ('graduating_date', )
        widgets = {
            'grade': forms.Select(attrs={'class': 'form-input', 'style': 'width: 100px;'}, choices=GRADE_CHOICES),
            'subject': forms.Select(attrs={'class': 'form-input', }),
            'student': forms.Select(attrs={'class': 'form-input', 'style': 'width: 300px;'}),
        }
