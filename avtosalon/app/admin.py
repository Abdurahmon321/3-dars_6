from django.contrib import admin

# Register your models here.
from .models import Category, Car, Customer, Employee, Color


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category")
    list_display_links = ("category",)


class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "color", "price", "quantity", "category", "max_speed", "discription",)
    list_display_links = ("name",)
    list_editable = ("category",)
    search_fields = ("name",)
    list_filter = ("name", "max_speed")


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "lastname", "phone_number", "email", "address")
    list_display_links = ("firstname",)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone_number", "email")


class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "color")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Employee, EmployeeAdmin)
