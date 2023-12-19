from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'post_photo', 'price', 'quantity', 'date_added')
    list_display_links = ('id', 'name')
    ordering = ['date_added', 'name']
    list_editable = ('price', 'quantity', )
    list_per_page = 5
    search_fields = ['title']

    @admin.display(description="Изображение")
    def post_photo(self, product: Product):
        if product.photo:
            return mark_safe(f"<img src='{product.photo.url}' width=50>")
        return "Без фото"

