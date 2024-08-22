from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'surname': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter your surname'}),
            'middle_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter your middle name'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'}),
            'district': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter your district'}),
            'village': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter your village'}),
            'gender': forms.Select(attrs={
                'class': 'form-select'}),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter your address'}),
            'disability': forms.Select(attrs={
                'class': 'form-select'}),
            'marital_status': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter your marital status'}),
            'institution_attended_a': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter institution name'}),
            'institution_attended_b': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter institution name'}),
            'institution_attended_c': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter institution name'}),
            'institution_attended_d': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter institution name'}),
            'course_of_study_a': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter course name'}),
            'course_of_study_b': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter course name'}),
            'course_of_study_c': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter course name'}),
            'qualification_a': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter qualification'}),
            'qualification_b': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter qualification'}),
            'qualification_c': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter qualification'}),
            'skill_a': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter skill'}),
            'skill_b': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter skill'}),
            'skill_c': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter skill'}),
            'experience_a': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter work experience'}),
            'experience_b': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter work experience'}),
            'experience_c': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter work experience'}),
        }
