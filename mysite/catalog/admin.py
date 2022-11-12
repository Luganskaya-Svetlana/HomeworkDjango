from django.contrib import admin

from .models import Category, GalleryImage, Item, Tag, MainImage


class MainImageInline(admin.TabularInline):
    model = MainImage
    readonly_fields = ('image_tmb',)
    fields = ('image', 'image_tmb')


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    readonly_fields = ('image_tmb',)
    fields = ('image', 'image_tmb')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ('name', 'text', 'category', 'tags', 'is_published')
    summernote_fields = ('text',)
    # summernote_fields = '__all__'
    inlines = (MainImageInline, GalleryImageInline)
    list_display = ('name', 'is_published', 'main_image_tmb',)
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


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('image_tmb', 'item')


@admin.register(MainImage)
class MainImageAdmin(admin.ModelAdmin):
    list_display = ('image_tmb', 'item')
