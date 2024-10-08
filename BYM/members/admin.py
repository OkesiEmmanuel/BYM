from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'email', 'phone_number', 'district', 'village', 'gender')
    search_fields = ('first_name', 'surname', 'email', 'phone_number', 'village')
    list_filter = ('gender', 'disability', 'marital_status', 'district', 'village')
    ordering = ('first_name', 'surname')
