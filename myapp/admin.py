from django.contrib import admin
from .models import Product, Category, Tag

# Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "product_list")
    search_fields = ("name",)

    def product_list(self, obj):
        return ", ".join([p.name for p in obj.products.all()])
    product_list.short_description = "Products"

# Product admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "tag_list")
    search_fields = ("name", "tags__name")  # correct ManyToMany search
    list_filter = ("category", "tags")      # filter sidebar

    def tag_list(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    tag_list.short_description = "Tags"

# Tag admin
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name",)
    list_filter = ("products",)  # filter tags by products

# Register models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
