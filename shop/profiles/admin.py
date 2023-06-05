from django.contrib import admin

from profiles.models import Profile, Address


@admin.register(Profile)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "created_at")
    fields = ("user", "first_name", "last_name", "age", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("first_name", "last_name")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "country", "city", "address", "created_at")
    fields = ("user", "country", "city", "address", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user", "address")
