from django.contrib import admin

from shop.models import Factory, Product, Retail, Entrepreneur


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'user_city', 'get_sum', 'factory', 'name')
    list_filter = ('user__city',)
    actions = ['reset_sum']

    def user_city(self, obj):
        return obj.user.city
    user_city.short_description = 'Город пользователя'

    @admin.action(description='Списание задолженности')
    def reset_sum(self, request, queryset):
        queryset.update(quantity=0)

    def get_sum(self, obj):
        return obj.sum()
    get_sum.short_description = 'Сумма'


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'user_city', 'get_sum', 'factory', 'name', 'retail','quantity')
    list_filter = ('user__city',)
    actions = ['reset_sum']

    def user_city(self, obj):
        return obj.user.city
    user_city.short_description = 'Город пользователя'

    @admin.action(description='Списание задолженности')
    def reset_sum(self, request, queryset):
        queryset.update(quantity=0)

    def get_sum(self, obj):
        return obj.sum()
    get_sum.short_description = 'Сумма'
