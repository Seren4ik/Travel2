from django.contrib import admin

from Cities.models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(City, CityAdmin)
