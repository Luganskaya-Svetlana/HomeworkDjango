from catalog.models import Item, Category
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404


class ItemsView(ListView):
    model = Item
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.published().order_by('category', 'name')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Список товаров'
        return data


class ItemView(DetailView):
    model = Item
    template_name = 'catalog/item_detail.html'
    context_object_name = 'item'

    def get_queryset(self):
        return Item.objects.published()


class ItemCategoryView(ListView):
    model = Item
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        slug = self.kwargs['slug']
        self.category = get_object_or_404(Category, slug=slug)
        return Item.objects.published().filter(category=self.category)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'Товары с категорией "{str(self.category)}"'
        return data


class CategoriesView(ListView):
    model = Category
    template_name = 'catalog/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.published()
