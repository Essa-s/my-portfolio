from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

# Create your models here.
class BasicInfo(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    job_1 = models.CharField(max_length=25)
    job_2 = models.CharField(max_length=25, blank=True)
    job_3 = models.CharField(max_length=25, blank=True)
    age = models.IntegerField()
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    phone_1 = models.IntegerField()
    phone_2 = models.IntegerField(blank=True)
    email_1 = models.EmailField(max_length=254)
    email_2 = models.EmailField(max_length=254, blank=True)
    website = models.URLField(max_length=200, blank=True)
    address = models.CharField(max_length=50)
    avilable = models.BooleanField()
    linkedin = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    instgram = models.URLField(max_length=200, blank=True)
    profile_picture = models.ImageField(upload_to='profile', height_field=None, width_field=None, max_length=None)
    about = models.TextField(blank=True)


    def save(self, *args, **kwargs):
        self.pk = 1  # Set primary key to 1 (or any other constant value)
        existing_instance = self.__class__.objects.first()
        if existing_instance:
            self.id = existing_instance.id  # Use the existing instance's ID
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Skill(models.Model):
    title = models.CharField(max_length=25)
    rate = models.IntegerField(
                validators=[
            MinValueValidator(1, message='Rate must be at least 1.'),
            MaxValueValidator(5, message='Rate cannot be greater than 5.')
        ]
    )
    detail = models.TextField()
    def __str__(self):
        return self.title
    
class Education(models.Model):
    degree = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    present = models.BooleanField()
    graduate_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    certifcate = models.ImageField(upload_to='education', height_field=None, width_field=None, max_length=None)
    detail = models.TextField()
    def clean(self):
        if self.present:
            self.graduate_date = None  # Set graduate_date to None if present is checked
        elif not self.graduate_date:
            raise ValidationError({'graduate_date': 'Graduation date is required if not present.'})

        return super().clean()
    def __str__(self):
        return f"{self.degree}-{self.major}"

class Course(models.Model):
    title = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    present = models.BooleanField()
    graduate_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    certifcate = models.ImageField(upload_to='courses', height_field=None, width_field=None, max_length=None)
    detail = models.TextField()
    def clean(self):
        if self.present:
            self.graduate_date = None  # Set graduate_date to None if present is checked
        elif not self.graduate_date:
            raise ValidationError({'graduate_date': 'Graduation date is required if not present.'})

        return super().clean()
    
    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    present = models.BooleanField()
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    certifcate = models.ImageField(upload_to='courses', height_field=None, width_field=None, max_length=None)
    def clean(self):
        if self.present:
            self.end_date = None  # Set graduate_date to None if present is checked
        elif not self.end_date:
            raise ValidationError({'graduate_date': 'Graduation date is required if not present.'})

        return super().clean()
    responsiblity_1 = models.CharField(max_length=200)
    responsiblity_2 = models.CharField(max_length=200, blank=True)
    responsiblity_3 = models.CharField(max_length=200, blank=True)
    responsiblity_4 = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.title

class Fact(models.Model):
    fact = models.CharField(max_length=50)
    number = models.IntegerField()
    emoji = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.fact

class Service(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField()
    emoji = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.CharField(max_length=50)
    detail = models.TextField()
    link = models.URLField(max_length=200)
    image_1 = models.ImageField(upload_to='projects', height_field=None, width_field=None, max_length=None)
    image_2 = models.ImageField(upload_to='projects', height_field=None, width_field=None, max_length=None)
    image_3 = models.ImageField(upload_to='projects', height_field=None, width_field=None, max_length=None)
