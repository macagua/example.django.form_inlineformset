# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _


class Recipe(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'), )

    def get_absolute_url(self):
        return '/recipes/{}/'.format(self.id)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Recipe')
        verbose_name_plural = _('Recipes')


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, verbose_name=_("Recipe"))
    description = models.CharField(_('Description'), max_length=255)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')


class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, verbose_name=_("Recipe"))
    number = models.PositiveSmallIntegerField(_('Number'), help_text=_('Step number'))
    description = models.TextField(_('Description'), )

    def __str__(self):
        return _("Step {number}: {description}").format(
            number=self.number,
            description=self.description
        )

    class Meta:
        verbose_name = _('Instruction')
        verbose_name_plural = _('Instructions')
