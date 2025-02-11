from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address',)
    readonly_fields = ['created_at',]
    list_display = ('town',
                    'price',
                    'address',
                    'new_building',
                    'construction_year',)
    list_editable = ('new_building',)
    list_filter = ('new_building',)


admin.site.register(Flat, FlatAdmin)
