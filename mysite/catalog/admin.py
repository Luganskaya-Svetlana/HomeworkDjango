from django.contrib import admin

from .models import Category, Gallery, Item, Tag


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ('name', 'text', 'category', 'tags', 'is_published', 'image')
    list_display = ('name', 'is_published', 'image_tmb')
    list_editable = ('is_published',)
    list_display_links = ('name',)
    filter_horizontal = ('tags',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'is_published')
    list_display = ('name', 'is_published')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'weight', 'is_published')
    list_display = ('name', 'is_published')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image_tmb', 'item')
