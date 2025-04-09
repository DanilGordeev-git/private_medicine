from django.contrib import admin
from .models import ServiceCategory, Service

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'available', 'order')
    list_filter = ('category', 'available')
    list_editable = ('price', 'available', 'order')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('category', 'title', 'slug', 'available', 'order')
        }),
        ('Описание', {
            'fields': ('short_description', 'full_description', 'advantages')
        }),
        ('Детали', {
            'fields': ('price', 'duration', 'image')
        }),
    )