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
    # inlines = [RelationshipInline]
    pass






    # formset = [RelationshipInlineFormset]