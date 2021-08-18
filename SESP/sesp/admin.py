from django.contrib import admin
from .models import Store, Entry, Exit

# Register your models here.

@admin.register(Store)
class Store(admin.ModelAdmin):
    readonly_fields = ["actual_people", "is_full"]
    pass


admin.site.register(Entry)
admin.site.register(Exit)

