from django.contrib import admin
from hw_app.models import Product, Client, Order

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'quantity', 'price']
    ordering = ['-quantity']
    list_filter = ['date_add', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта(description)'
    actions = [reset_quantity]

    """Отдельный продукт."""
    # fields = ['name', 'description', 'category', 'quantity', 'date_add', 'rating']
    readonly_fields = ['date_add', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_add'],
            }
        ),
    ]


class ClientAdmin(admin.ModelAdmin):
    """Список клиентов."""
    list_display = ['name', 'phone', 'email']
    ordering = ['name', 'phone']
    list_filter = ['name', 'date_registration']
    search_fields = ['name', 'phone', 'email']

    """Отдельный клиент."""
    # fields = ['name', 'description', 'category', 'quantity', 'date_add', 'rating']
    readonly_fields = ['date_registration']

class OrderAdmin(admin.ModelAdmin):
    # list_display = ['customer', 'products', 'total_price']
    list_display = [field.name for field in Order._meta.get_fields() if not field.many_to_many]


    readonly_fields = ['date_ordered']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order,OrderAdmin)

