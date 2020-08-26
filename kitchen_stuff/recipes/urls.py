from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    # /
    path('', views.recipes_list, name='list'),
    # /recipes/register/
    path(
        'recipes/register/',
        views.recipes_register_edition,
        name='register'
    ),
    # /recipes/1/
    path(
        'recipes/<int:recipe_id>/',
        views.recipes_detail,
        name='detail'
    ),
    # /recipes/1/edit
    path(
        'recipes/<int:recipe_id>/edit',
        views.recipes_register_edition,
        name='edit'
    ),
    # /recipes/1/delete
    path(
        'recipes/<int:recipe_id>/delete',
        views.recipes_delete,
        name='delete'
    ),
]
