from django.contrib import admin

from .models import Address, Phone


# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fields = (
        'state',
        'city',
        'neighborhood',
        'street',
        'number',
        'complement',
        'cep',
    )
    list_filter = (
        'state',
        'neighborhood',
    )
    list_display = (
        'state',
        'city',
        'neighborhood',
        'street',
        'number',
        'complement',
        'cep',
    )
    ordering = ('email',)
    search_fields = (
        'username',
        'email',
    )

    list_max_show_all = 100


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    fields = (
        'DDD',
        'number',
        'user',
        'supplier',
    )
    list_filter = (
        'DDD',
        'user',
        'supplier',
    )
    list_display = (
        'DDD',
        'number',
        'user',
        'supplier',
    )
    ordering = ('email',)
    search_fields = (
        'number',
        'user',
        'supplier',
    )


class AddressInline(admin.TabularInline):
    model = Address


class PhoneInline(admin.TabularInline):
    model = Phone
