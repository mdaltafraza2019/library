from django.contrib import admin
from .models import*
from django.utils.html import format_html
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('course',)}

class ShiftAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('shift_title',)}

admin.site.register(Student)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Shift,ShiftAdmin)
