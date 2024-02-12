from django.contrib import admin
from .models import BasicInfo, Skill, Course, Education, Experience, Fact, Service, Project
# Register your models here.
admin.site.register(BasicInfo)
admin.site.register(Skill)
admin.site.register(Course)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Fact)
admin.site.register(Service)
admin.site.register(Project)