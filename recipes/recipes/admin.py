# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Recipe, Ingredient, Instruction


# Register models:
# https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.StackedInline
# https://stackoverflow.com/questions/4890981/django-admin-stackedinline-customisation
# class RecipeInline(admin.StackedInline):
#     model = Recipe


class IngredientInline(admin.TabularInline):
    model = Ingredient
    min_num = 2


class InstructionInline(admin.TabularInline):
    model = Instruction
    min_num = 0


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [IngredientInline, InstructionInline]


admin.site.register(Recipe, RecipeAdmin)
# admin.site.register(Ingredient)
# admin.site.register(Instruction)
