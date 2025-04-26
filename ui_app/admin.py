from django.contrib import admin
from django.utils.html import format_html

from .models import CustomUser, Book
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительная информация", {"fields": ("avatar",)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'cover_preview')
    search_fields = ('title', 'author')

    def cover_preview(self, obj):
        if obj.cover:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.cover.url)
        return "-"
    cover_preview.short_description = "Обложка"