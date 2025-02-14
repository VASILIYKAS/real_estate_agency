from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatsInline(admin.TabularInline):
    model = Flat.flats.through
    raw_id_fields = ('owner',)


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
    inlines = [FlatsInline]


admin.site.register(Flat, FlatAdmin)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


admin.site.register(Complaint, ComplaintAdmin)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owner_flats',)


admin.site.register(Owner, OwnerAdmin)
