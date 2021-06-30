from django.contrib import admin
from .models import Product, Category, ProductIndex
from client.models import User


class ProductIndexAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        "boot",
        'name_uz',
        'name_ru',
        "price2",
        'price',
        'photo',

    ]
    class Meta:
        model = ProductIndex

admin.site.register(ProductIndex, ProductIndexAdmin)










class UserAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'username',
        'first_name',
        'last_name',
        'date_joined',
        'is_staff',
        'is_superuser'
    ]

    class Meta:
        model = User


admin.site.register(User, UserAdmin)



class CategoryAdmin(admin.ModelAdmin):

    fields = [
        'parent',
        'name_uz',
        'name_ru'

    ]

    list_display = [
        'id',
        "name_uz",
        "name_ru",
        'parent',
        "added_at",
        "updated_at"

    ]


    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)




class ProductAdmin(admin.ModelAdmin):

    list_display = [
        "name_uz",
        "name_ru",
        "price",
        "photo",
        "status",
        "category_id",
    ]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)