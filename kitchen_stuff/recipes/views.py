from django.forms.models import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _

from .models import Recipe, Ingredient, Instruction
from .forms import RecipeForm


def recipes_list(request):
    template_name = "recipes/recipes_list.html"
    recipes = Recipe.objects.all()
    context = {'recipes': recipes,}
    return render(request, template_name, context)


def recipes_detail(request, recipe_id=None):
    template_name = "recipes/recipes_detail.html"
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
        context = {'recipe': recipe}
    except Recipe.DoesNotExist:
        raise Http404(_("Recipe does not exist"))
    return render(request, template_name, context)


def recipes_register_edition(request, recipe_id=None):
    template_name = "recipes/register_edition.html"
    if recipe_id:
        recipe = Recipe.objects.get(pk=recipe_id)
    else:
        recipe = Recipe()

    IngredientFormSet = inlineformset_factory(Recipe, Ingredient, fields='__all__', extra=0, can_delete=True)
    InstructionFormSet = inlineformset_factory(Recipe, Instruction, fields='__all__', extra=0, can_delete=True)

    if request.method == 'POST':
        form = RecipeForm(request.POST or None, instance=recipe)
        ingredientFormset = IngredientFormSet(request.POST or None, instance=recipe)
        instructionFormset = InstructionFormSet(request.POST or None, instance=recipe)

        if form.is_valid() and ingredientFormset.is_valid() and instructionFormset.is_valid():
            form.save()
            ingredientFormset.save()
            instructionFormset.save()
            return redirect('recipes:list')
    else:
        form = RecipeForm(instance=recipe)
        ingredientFormset = IngredientFormSet(instance=recipe)
        instructionFormset = InstructionFormSet(instance=recipe)

    return render(request, template_name)


def recipes_delete(request, recipe_id=None):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    if recipe.delete():
        return redirect('recipes:list')
