from django.contrib import admin

from .models import Department
from .models import DataType
from .models import Project

admin.site.register(Department)
admin.site.register(DataType)
admin.site.register(Project)
