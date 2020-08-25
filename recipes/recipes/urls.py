from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.recipes_list, name='recipes-list'),
    url(r'^recipes/register/$', views.recipes_register_edition, name='recipes-register'),
    url(r'^recipes/(?P<recipe_id>\d+)/$', views.recipes_register_edition, name='recipes-edit'),
]
