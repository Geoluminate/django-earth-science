from .models import Plate
from django.contrib.gis import admin


@admin.register(Plate)
class Plate(admin.GeoModelAdmin):
    change_list_template = 'admin/gis/change_list.html'

    list_display = [
        'name', 'subplate', 'plate', 'type',
        'crust_type', 'domain', 'area']

    search_fields = ['name', 'subplate',]

    list_filter = ['plate', 'type', 'crust_type', 'domain']
    fields = ['geom',
              'id', 'name', 'plate', 'plate_id', 'poly_name', 'type',
              'crust_type', 'domain']
