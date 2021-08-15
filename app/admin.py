from django.contrib import admin

from .models import Employee, Contact, MynumberCard

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('pk','name', 'age')

class ContactAdmin(admin.ModelAdmin):
    list_display=('pk','phoneNumber','address','employee')

class MynumberCardAdmin(admin.ModelAdmin):
    list_display=('pk','number', 'employee')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(MynumberCard, MynumberCardAdmin)
