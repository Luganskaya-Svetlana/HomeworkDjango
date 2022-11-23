from catalog.models import Item
from django.shortcuts import render


def home(request):
    template_name = 'homepage/homepage.html'
    items = Item.objects.published().order_by('name').filter(is_on_main=True)
    context = {'items': items, }
    return render(request, template_name, context)
