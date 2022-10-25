from django.http import HttpResponse


def item_list(request):
    return HttpResponse('Список прекрасных элементов')


def item_detail(request, pk):
    return HttpResponse(f'Подробно о прекрасном элементе с primary key {pk}')
