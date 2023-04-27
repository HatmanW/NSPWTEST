from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


class EntityAdmin(admin.ModelAdmin):
    ...
    list_filter = (
        # for ordinary fields
        ('a_charfield', DropdownFilter),
        # for choice fields
        ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('a_foreignkey_field', RelatedDropdownFilter),
    )