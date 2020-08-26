from django.contrib import admin
from .models import Recipe, Ingredient, Instruction


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
