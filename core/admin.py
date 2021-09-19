from django.contrib import admin
from .models import *


class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'address', 'categories', 'websites'
    )


admin.site.register(Store, StoreAdmin)
admin.site.register(Address)
admin.site.register(Categories)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Province)
