from catalog.models import Item
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class ItemsView(ListView):
    model = Item
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.published().order_by('category', 'name')


class ItemView(DetailView):
    model = Item
    template_name = 'catalog/item_detail.html'
    context_object_name = 'item'

    def get_queryset(self):
        return Item.objects.published()
