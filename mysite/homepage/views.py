from catalog.models import Item
from django.views.generic.list import ListView


class Homepage(ListView):
    model = Item
    template_name = 'homepage/homepage.html'
    context_object_name = 'items'

    def get_queryset(self):
        return (Item.objects.published().order_by('name')
                                        .filter(is_on_main=True))
