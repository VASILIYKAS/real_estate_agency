from django.contrib import admin

from .models import Flat, Complaint


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
    raw_id_fields = ('liked_by',)


admin.site.register(Flat, FlatAdmin)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


admin.site.register(Complaint, ComplaintAdmin)
