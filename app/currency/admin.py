from django.contrib import admin
import currency.models as models


# Register your models h
@admin.register(models.Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'buy',
        'sell',
        'currency',
        'source',
        'created'
    )
    list_filter = (
        'currency',
        'created'
    )
    readonly_fields = (
        # 'buy',
        # 'sell',
    )

    def has_delete_permission(self, request, obj=None):
        return False


# admin.site.register(models.Rate, RateAdmin)
@admin.register(models.Source)
class SourceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ContactUS)
class ContactUSAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
