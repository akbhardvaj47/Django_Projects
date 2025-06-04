from django.shortcuts import render
from .models import Recipe

def recipe(request):
    recipe_list=Recipe.objects.all()
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_desc = request.POST.get('recipe_desc')
        recipe_image = request.FILES.get('recipe_image')

        if recipe_name:
            Recipe.objects.create(
                recipe_name=recipe_name,
                recipe_desc=recipe_desc,
                recipe_image=recipe_image
            )
    return render(request, 'recipes.html',{'recipe_list':recipe_list})
