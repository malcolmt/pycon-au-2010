from django.contrib import admin

from phm_collection import models

class ItemAdmin(admin.ModelAdmin):
    raw_id_fields = ["categories"]

class CategoryAdmin(admin.ModelAdmin):
    ordering = ["name"]

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Item, ItemAdmin)

