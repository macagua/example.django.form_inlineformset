from django.shortcuts import render_to_response as render, redirect
from django.template import RequestContext as ctx
from django.forms.models import inlineformset_factory

from .models import Recipe, Ingredient, Instruction
from .forms import RecipeForm


def recipes_list(request):
    template_name = "recipes_list.html"
    recipes = Recipe.objects.all()

    return render(template_name, locals(),
        context_instance=ctx(request))


def recipes_detail(request, recipe_id=None):
    template_name = "recipes_detail.html"
    if recipe_id:
        recipe = Recipe.objects.get(pk=recipe_id)
        context = {'recipe': recipe}

    return render(template_name, locals(),
        context_instance=ctx(request))



def recipes_register_edition(request, recipe_id=None):
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
            #return redirect('recipes-list')
            return redirect('/')
    else:
        form = RecipeForm(instance=recipe)
        ingredientFormset = IngredientFormSet(instance=recipe)
        instructionFormset = InstructionFormSet(instance=recipe)

    return render('register_edition.html', locals(),
        context_instance=ctx(request))
