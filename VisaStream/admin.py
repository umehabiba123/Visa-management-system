from django.contrib import admin
from .models import Application
# Register your models he







@admin.register(Application)   
class ApplicationAdminModel(admin.ModelAdmin):
    list_display = ["family_name",
        "given_names",
        "nationality",

    ]