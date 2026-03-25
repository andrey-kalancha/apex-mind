from django.contrib import admin
from .models import PartnerRequest, SurveyResponse


@admin.register(PartnerRequest)
class PartnerRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'position', 'phone', 'email', 'created_at')
    search_fields = ('name', 'company', 'position', 'phone', 'email')
    list_filter = ('created_at',)


@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'created_at')
    search_fields = ('company', 'position')
    list_filter = ('created_at',)