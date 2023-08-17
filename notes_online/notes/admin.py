from django.contrib import admin

from .models import Theme, Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "topic", "name", "created_at", "updated_at")
    list_display_links = ("id", "topic", "name")
    search_fields = ("name", "text")
    list_filter = ("topic", "created_at", "updated_at")



class ThemeAdmin(admin.ModelAdmin):
    list_display = ("id", "theme_name", "created_at", "updated_at")
    list_display_links = ("id", "theme_name")
    search_fields = ("theme_name",)
    list_filter = ("created_at", "updated_at")



# Register your models here.
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Note, NoteAdmin)
