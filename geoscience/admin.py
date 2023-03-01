from django.contrib import admin
from .models import EarthMaterial, GeologicTime
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from django.core.paginator import Paginator
from .filters import TreeNodeDepthFilter
from django.utils.html import mark_safe

# Register your models here.
class EarthMaterialTreeAdmin(TreeAdmin):
    form = movenodeform_factory(EarthMaterial)
    node_filter_depth = 2
    search_fields = [
        'name','code',
    ]

class EarthMaterialAdmin(admin.ModelAdmin):
    form = movenodeform_factory(EarthMaterial)
    list_display = ['name','code','description']
    # list_filter = ['status','depth']
    search_fields = [
        'name','code', 
    ]


class GeoTimeTreeAdmin(TreeAdmin):
    form = movenodeform_factory(GeologicTime)
    node_filter_depth = 2
    list_per_page = 200
    search_fields = [
        'label',
    ]

class GeoTimeAdmin(admin.ModelAdmin):
    form = movenodeform_factory(GeologicTime)
    list_display = ['rank','label','status','younger_bound','older_bound','_about']
    list_per_page = 200
    list_filter = ['rank','status',]
    search_fields = ['label',]

    def _about(self, obj):
        return mark_safe(f"<a href='{obj.about}'>{obj.about}</a>")
    _about.short_description = 'About'
    _about.admin_order_field = 'about'

# admin.site.register(GeologicTime, GeoTimeTreeAdmin)
admin.site.register(GeologicTime, GeoTimeAdmin)

# admin.site.register(EarthMaterial, EarthMaterialTreeAdmin)
# admin.site.register(EarthMaterialProxy, EarthMaterialAdmin)