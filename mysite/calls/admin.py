from django.contrib import admin

from .models import Call, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("line", "cost")


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ("id", "duration", "category", "cost")
    list_filter = ("category", "created_on")
    readonly_fields = ("cost",)
