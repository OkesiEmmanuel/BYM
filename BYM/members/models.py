from django.db import models

class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    DISABILITY_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField()
    district = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    disability = models.CharField(max_length=1, choices=DISABILITY_CHOICES)
    marital_status = models.CharField(max_length=50)

    institution_attended_a = models.CharField(max_length=255, blank=True)
    institution_attended_b = models.CharField(max_length=255, blank=True)
    institution_attended_c = models.CharField(max_length=255, blank=True)

    course_of_study_a = models.CharField(max_length=255, blank=True)
    course_of_study_b = models.CharField(max_length=255, blank=True)
    course_of_study_c = models.CharField(max_length=255, blank=True)

    qualification_a = models.CharField(max_length=255, blank=True)
    qualification_b = models.CharField(max_length=255, blank=True)
    qualification_c = models.CharField(max_length=255, blank=True)

    skill_a = models.CharField(max_length=255, blank=True)
    skill_b = models.CharField(max_length=255, blank=True)
    skill_c = models.CharField(max_length=255, blank=True)

    experience_a = models.CharField(max_length=255, blank=True)
    experience_b = models.CharField(max_length=255, blank=True)
    experience_c = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"
