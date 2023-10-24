from django.contrib import admin

from django.forms import BaseInlineFormSet
from .models import Measurements, Sensor


@admin.register(Measurements)
class MesAdmin(admin.ModelAdmin):
    pass
# class RelationshipInline(admin.TabularInline):
#     model = Measurements
#     extra = 1


@admin.register(Sensor)
class ObjectAdmin(admin.ModelAdmin):
    list_filter = ['id', 'name', 'description']
    # list_filter = ['id','name','description','measurement']
    # inlines = [RelationshipInline]





