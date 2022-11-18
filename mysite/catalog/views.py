from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Item


def item_list(request):
    template_name = 'catalog/item_list.html'
    items = Item.objects.published().order_by('category')
    context = {'items': items, }
    return render(request, template_name, context)


def item_detail(request, pk):
    return HttpResponse(f'Подробно о прекрасном элементе с primary key {pk}')
