from django.http import HttpResponse
from django.shortcuts import render


def item_list(request):
    template_name = 'catalog/item_list.html'
    return render(request, template_name)


# def item_list(request):
#     return HttpResponse('Список прекрасных элементов')


def item_detail(request, pk):
    return HttpResponse(f'Подробно о прекрасном элементе с primary key {pk}')
