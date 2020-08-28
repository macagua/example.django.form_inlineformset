from django.contrib import messages
from django.forms.models import inlineformset_factory
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .models import Ingredient, Instruction, Recipe
from .forms import RecipeForm


def recipes_list(request):
    ''' list view for recipes '''

    # dictionary for initial data with field names as keys
    context = {}
    # template name for recipe list view
    template_name = "recipes/recipes_list.html"
    # fetch all recipes
    recipes = Recipe.objects.all()

    context = {'recipes': recipes,}
    return render(request, template_name, context)


def recipes_detail(request, recipe_id=None):
    ''' detail view for a recipe '''

    # dictionary for initial data with field names as keys
    context = {}
    # template name for recipe detail view
    template_name = "recipes/recipes_detail.html"

    try:
        # fetch the recipe related to passed id
        recipe = Recipe.objects.get(pk=recipe_id)
        # fetch the ingredients related to recipe id
        ingredients = recipe.ingredient_set.filter(recipe=recipe.id)
        # fetch the instructions related to recipe id
        instructions = recipe.instruction_set.filter(recipe=recipe.id).order_by('number')
    except Recipe.DoesNotExist:
        raise Http404(_("Recipe does not exist"))
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
        'instructions': instructions,
    }
    return render(request, template_name, context)


def recipes_register_edition(request, recipe_id=None):
    ''' register and edition view for recipe '''

    # dictionary for initial data with field names as keys
    context = {}
    # template name for recipe register and edition view
    template_name = "recipes/register_edition.html"

    if recipe_id:
        # fetch the recipe related to passed id
        recipe = Recipe.objects.get(pk=recipe_id)
    else:
        # create the new recipe
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
            # message to show when save was success
            messages.success(request, _("Recipe successfully saved!"))
            return redirect('recipes:detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
        ingredientFormset = IngredientFormSet(instance=recipe)
        instructionFormset = InstructionFormSet(instance=recipe)

    context = {
        'form': form,
        'ingredientFormset': ingredientFormset,
        'instructionFormset': instructionFormset,
    }

    return render(request, template_name, context)


def recipes_delete(request, recipe_id=None):
    ''' delete view for recipe detail '''

    # dictionary for initial data with field names as keys
    context = {}
    # template name for a confirm delete recipe view
    template_name = 'recipes/recipes_confirm_delete.html'
    # fetch the recipe related to passed id
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {'recipe': recipe}

    if request.method == "POST":
        # delete object
        recipe.delete()
        # message to show when delete was success
        messages.success(request, _("Recipe successfully deleted!"))
        # after deleting redirect to recipe list page
        return HttpResponseRedirect(reverse('recipes:list'))

    return render(request, template_name, context)
