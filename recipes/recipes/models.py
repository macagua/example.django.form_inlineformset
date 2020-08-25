from django.db import models
from django.utils.translation import gettext_lazy as _


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def get_absolute_url(self):
        return '/recipes/{}/'.format(self.id)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Recipe')
        verbose_name_plural = _('Recipes')


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')


class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe)
    number = models.PositiveSmallIntegerField(help_text=_('Step number'))
    description = models.TextField()

    def __str__(self):
        return "%s - %s" % (self.number, self.description)

    class Meta:
        verbose_name = _('Instruction')
        verbose_name_plural = _('Instructions')
